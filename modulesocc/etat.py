from soccersimulator import Vector2D, SoccerState, SoccerAction
from soccersimulator import Simulation, SoccerTeam, Player, show_simu
from soccersimulator import Strategy
from soccersimulator import settings
from soccersimulator.settings import *
import math

class Etat(object):
	def __init__(self,state,id_team,id_player):
		self.state = state
		self.id_team = id_team
		self.id_player = id_player
	
	def posballe(self) :
		return self.state.ball.position
	
	def posjoueur(self) :
		return self.state.player_state(self.id_team,self.id_player).position
	
	def speed(self) :
		return self.state.ball.vitesse

	def posgoal(self) :
		if self.id_team==1:
			pos=Vector2D(GAME_WIDTH,GAME_HEIGHT/2)
		if self.id_team==2:
			pos=Vector2D(0,GAME_HEIGHT/2)
		return pos

	def distballe(self) :
		posb=self.posballe()
		posj=self.posjoueur()
		return math.hypot(posb.x-posj.x,posb.y-posj.y)

	def posdef(self) :
		posb=self.posballe()

	def estcentre(self) :
		posb=self.posballe()
		return (posb.x==GAME_WIDTH/2 and posb.y==GAME_HEIGHT/2)
