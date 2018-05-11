from soccersimulator import Vector2D, SoccerState, SoccerAction
from soccersimulator import Simulation, SoccerTeam, Player, show_simu
from soccersimulator import Strategy
from soccersimulator import settings
from soccersimulator.settings import *
from .actions_simples import *
from .etat import *
import math
from random import *


#Fonce vers la balle, tire toujours à une force = shoot
def fonceur_defaut(state,id_t,id_p, shoot) :
	e=Etat(state)
	if e.can_shoot(id_t,id_p) :
		return SoccerAction(dirballe(e,id_t,id_p, 1, 0), dirgoal(e, id_t%2+1, shoot, (0.8-0.2)*random()+0.2))
	else :
		return SoccerAction(dirballe(e,id_t,id_p, 1, 10))

#dribble basique
def dribble(state,id_t,id_p) :
	e=Etat(state)
	if e.can_shoot(id_t,id_p) :
		return SoccerAction(dirballe(e,id_t,id_p, 1, 0), dirgoal(e, id_t%2+1, 2, 0.5))
	else :
		return SoccerAction(dirballe(e,id_t,id_p, 1, 10))

#dribble évitant les adversaires
def dribble2(state,id_t,id_p) :
	e=Etat(state)
	posj=e.posjoueur(id_t,id_p)
	posj_adv=e.posjoueur(id_t%2+1,e.proche_balle(id_t%2+1))
	if e.can_shoot(id_t,id_p) :
		if not(e.trajectoire_adv(id_t)) :
			return SoccerAction(dirballe(e,id_t,id_p, 1, 0), dirgoal(e, id_t%2+1, 2, 0.5))			
		elif e.trajectoire_adv(id_t) and e.trajectoire_goal(id_t) :
			dir_goal=dirgoal(e, id_t%2+1, 2, 0.2)
			if posj_adv.y>posj.y :
				dir_goal.angle += math.radians(40)
			else :
				dir_goal.angle -= math.radians(40)
			return SoccerAction(dirballe(e,id_t,id_p, 1, 0), dir_goal)
		elif e.trajectoire_adv(id_t) and not(e.trajectoire_goal(id_t)) :
			dir_goal=dirgoal(e, id_t%2+1, 2, 0.8)
			if posj_adv.y>posj.y :
				dir_goal.angle -= math.radians(60)
			else :
				dir_goal.angle += math.radians(60)
			return SoccerAction(dirballe(e,id_t,id_p, 1, 0), dir_goal)
		else :
			return SoccerAction(dirballe(e,id_t,id_p, 1, 0), dirgoal(e, id_t%2+1, 2, 0.5))			
	else :
		return SoccerAction(dirballe(e,id_t,id_p, 1, 10))


#Reste en défense, fait la passe au joueur allié le plus proche
def defense(state,id_t,id_p, shoot):
	e=Etat(state)
	posb=e.posballe()
	posg=e.poscage(id_t)
	posj=e.posjoueur(id_t,id_p)
	#le défenseur ira vers la balle si il est le plus proche, si la balle est trop proche des cages
	#ou si la balle est très éloignée des cages
	if (not(e.adv_prox(id_t,id_p)) and e.dist(posg,posb)<GAME_WIDTH/2.05) :
		nb_j=e.proche_joueur(id_t,id_p)
		if e.can_shoot(id_t,id_p) and nb_j != id_p : #le défenseur passe la balle à un équipier
			return SoccerAction(dirballe(e,id_t,id_p, 1, 0), passedef(e,id_t,nb_j, shoot, 1))
		elif e.can_shoot(id_t,id_p) and nb_j== id_p : #le défenseur n'a pas de coéquipier
			return SoccerAction(dirballe(e,id_t,id_p, 1, 0), dirgoal(e,id_t%2+1, shoot, 0.5))
		else :
			return SoccerAction(dirballe(e,id_t,id_p, 1, 2))
	elif e.balle_def(id_t%2+1, 0.4) and e.dist(posj,posb)<=50 :
		return fonceur_defaut(state,id_t,id_p,shoot)
	else : 
		return SoccerAction(dirpos(e,id_t, id_p, 1, e.posdef(id_t,0.4)))

#Attaque, receptionne les passes du défenseur (s'il y en a)
def attaque(state, id_t,id_p, shoot) :
	e=Etat(state)
	id_jd=e.proche_joueur(id_t,id_p)
	id_jb=e.proche_balle(id_t)
	posb=e.posballe()
	posg=e.poscage(id_t)
	if e.nb_joueurs(id_t)>1 and id_jb != id_p:
		vect = 	dirpos(e,id_t,id_p,1,e.pospasse(id_t, id_jd, 25))
		return SoccerAction(vect)
	else :
		if e.atteindre_balle(id_t,id_p,5) and e.dist(posg,posb)<GAME_WIDTH/2:
			return SoccerAction(dirpos(e,id_t, id_p, 1, e.posdef(id_t,0.3)))
		elif e.dist(e.posballe(),e.poscage(id_t%2+1))>=50 and e.dist(posb,Vector2D(GAME_WIDTH/2,GAME_HEIGHT/2))>5 :
			return dribble2(state,id_t,id_p)
		else :
			return fonceur_defaut(state, id_t, id_p, shoot)

#mini-strategie position de reception de passe
def recpasse(state, id_t, id_p):
	e=Etat(state)
	id_jd=e.proche_joueur(id_t,id_p)
	vect = 	dirpos(e,id_t,id_p,1,e.pospasse(id_t, id_jd, 25))
	return SoccerAction(vect)

#mini-strategie passe la balle
def fairepasse(state, id_t, id_p,shoot):
	e=Etat(state)
	nb_j=e.proche_joueur(id_t,id_p)
	if e.can_shoot(id_t,id_p):
		return SoccerAction(dirballe(e,id_t,id_p, 1, 0), passedef(e,id_t,nb_j, shoot, 1))
	else :
		return SoccerAction(dirballe(e,id_t,id_p, 1, 2))

#mini-strategie va en position defensive
def arriere(state, id_t, id_p):
	e=Etat(state)
	return SoccerAction(dirpos(e,id_t, id_p, 1, e.posdef(id_t,0.4)))

#mini-strategie fonce au centre pour dégager la balle dans le coin supérieur adverse
def foncer_centre(state, id_t, id_p, shoot):
	e=Etat(state)
	if e.can_shoot(id_t,id_p):
		return SoccerAction(dirballe(e,id_t,id_p,1,0),tirpos(e,coin(e,id_t,id_p),shoot))
	else:
		return SoccerAction(dirballe(e,id_t,id_p,1,0))

#mini-strategie se place pour intercepter la balle dégagée par le premier attaquant
def intercepte_centre(state,id_t,id_p):
	e=Etat(state)
	return SoccerAction(dirpos(e,id_t,id_p,1,pos_intercepte_c(e,id_t,id_p)))

#mini-strategie fonce au centre faire perdre du temps
def tempo_centre(state,id_t,id_p,shoot):
	e=Etat(state)
	posg=e.poscage(id_t%2+1)
	if e.can_shoot(id_t,id_p):
		return SoccerAction(dirballe(e,id_t,id_p,1,0),tirpos(e,Vector2D(posg.x,GAME_HEIGHT),shoot))
	else:
		return SoccerAction(dirballe(e,id_t,id_p,1,10))

#mini-strategie de feinte lors d'un dribble
def feinte(state,id_t,id_p):
	e=Etat(state)
	posb=e.posballe()
	dirg=dirgoal(e,id_t%2+1,4,0.5)
	sp=e.spballe()
	y=posb.y
	x=posb.x
	if e.can_shoot(id_t,id_p):
		if (x>GAME_WIDTH/2 and y>GAME_HEIGHT/2) or  (x<=GAME_WIDTH/2 and y<=GAME_WIDTH/2):
			if sp.angle+math.radians(5)/(dirg.angle+math.radians(5)) > 1 :
				dirg.norm=3
				dirg.angle-= math.radians(60)
				print("dévie")
			else :
				dirg.norm=0.8
				dirg.angle+=math.radians(30)
				print("feinte")
		else :
			if sp.angle+math.radians(5)/(dirg.angle+math.radians(5)) < 1 :
				dirg.norm=3
				dirg.angle-= math.radians(60)
				print("dévie")
			else :
				dirg.norm=0.8
				dirg.angle+=math.radians(30)
				print("feinte")
		return SoccerAction(dirballe(e,id_t,id_p,1,0),dirg)
	else:
		return SoccerAction(dirballe(e,id_t,id_p,1,10))
