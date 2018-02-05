from __future__ import absolute_import
from soccersimulator import Vector2D, SoccerState, SoccerAction
from soccersimulator import Simulation, SoccerTeam, Player, show_simu
from soccersimulator import Strategy
from soccersimulator import settings
from soccersimulator.settings import *
import math

class Etat(object):
	def __init__(self,state,id_team,id_player):
		self.state = state
		self.id_team=id_team
		self.id_player=id_player
	
	def posballe(self) :
		return self.state.ball.position
	
	def posjoueur(self) :
		return self.state.player_state(id_team,id_player).position
	
	def speed(self) :
		return self.state.ball.vitesse

	def distballe(self) :
		posb=posballe(self)
		posj=posjoueur(self)
		return math.hypot(posb.x-posj.x,posb.y-posj.y)

	def posdef(self) :
		posb=self.posballe()
		vect=Vector2D(0,0)
		if self.id_team==1:
			dirg=Vector2D(GAME_WIDTH,GAME_HEIGHT/2)-self.posballe()
		if self.id_team==2:
			dirg=Vector2D(0,GAME_HEIGHT/2)-self.posballe()
		posb.x=posb.x+dirg.x/2
		posb.y=posb.y+dirg.x/2
		return posb
