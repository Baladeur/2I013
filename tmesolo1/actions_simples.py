from soccersimulator import SoccerAction,Vector2D,settings ,SoccerTeam,Billard,show_simu,Strategy
from .etat import *
import math

#calcul position impact balle-goal
def impact(etat, nb) :
	posg=Vector2D(settings.GAME_WIDTH,settings.GAME_HEIGHT/2)
	posb=etat.posballs(nb)
	distance=etat.dist(posg,posb)
	facteur=(distance+0.9*settings.BALL_RADIUS)/distance #calcule la position sur la droite entre la balle grise et les cages, décalé de 0.9* le rayon de la balle derrière la balle grise.
	x=(posb.x-posg.x)*facteur+posg.x
	y=(posb.y-posg.y)*facteur+posg.y
	return Vector2D(x,y)

#Vecteur direction du joueur vers la position indiquée
def dirpos(etat, norme, pos) :
	vect= pos-etat.posjoueur()
	vect.norm = norme
	return vect

#position pour tirer dans la balle vers une balle nb
def pos_tir(etat, nb) :
	posb1=etat.posballe()
	posb=etat.posballs(nb)
	distance=etat.dist(posb1,posb)
	facteur=(distance+2*settings.BALL_RADIUS)/distance 
	x=(posb1.x-posb.x)*facteur+posb.x
	y=(posb1.y-posb.y)*facteur+posb.y
	return Vector2D(x,y)

#shoot la balle vers la position d'impact
def shootb(etat,nb) :
	return (impact(etat,nb)-etat.posballe())*100

#ralenti sur place
def ralenti(etat,nb) :
	vect=dirpos(etat,0.4,etat.posjoueur())
	vect.norm=0.05
	return vect
