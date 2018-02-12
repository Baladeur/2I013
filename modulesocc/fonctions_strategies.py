from soccersimulator import Vector2D, SoccerState, SoccerAction
from soccersimulator import Simulation, SoccerTeam, Player, show_simu
from soccersimulator import Strategy
from soccersimulator import settings
from soccersimulator.settings import *
from .actions_simples import *
from .etat import *
import math

def deviation(etat,norme) :
	direction_goal=dirgoal(etat,norme)
	sp=etat.speed()
	balle=etat.posballe()
	if sp.x>0:
		anticipe=balle.y+(direction_goal.x/sp.x)*sp.y
		if anticipe>=GAME_HEIGHT/2-GAME_GOAL_HEIGHT and anticipe<=GAME_HEIGHT/2+GAME_GOAL_HEIGHT:
			if balle.y >=GAME_HEIGHT/2:
				direction_goal.angle += math.radians(25)
			if balle.y <GAME_HEIGHT/2:
				direction_goal.angle -= math.radians(25)
	return direction_goal

def bait(etat) :
	if etat.estcentre() :
		dirb=dirpos(etat,1,etat.posinter())
	elif etat.balle_def() and etat.prox_balle() :
		dirb=dirpos(etat,1,etat.posdef())
	else :
		dirb=dirballe(etat,1)
	return dirb
