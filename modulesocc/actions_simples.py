from soccersimulator import Vector2D, SoccerState, SoccerAction
from soccersimulator import Simulation, SoccerTeam, Player, show_simu
from soccersimulator import Strategy
from soccersimulator import settings
from soccersimulator.settings import *
from .etat import *
import math

def dirballe(etat,norme) :
	vect = etat.posballe()-etat.posjoueur()
	vect.norm = norme
	return vect

def dirpos(etat,norme,pos):
	vect = pos-etat.posjoueur()
	vect.norm = norme
	return vect

def dirgoal(etat,norme) :
	vect=Vector2D(0,0)
	if etat.id_team==1:
		vect=Vector2D(GAME_WIDTH,GAME_HEIGHT/2)-etat.posballe()
	if etat.id_team==2:
		vect=Vector2D(0,GAME_HEIGHT/2)-etat.posballe()
	vect.norm=norme
	return vect


