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

	def posinter(self) :
		posb=self.posballe()
		if self.id_team==1:
			posb.x-=8
		if self.id_team==2:
			posb.x+=8
		return posb

	def estcentre(self) :
		posb=self.posballe()
		return (posb.x==GAME_WIDTH/2 and posb.y==GAME_HEIGHT/2)

	def posdef(self) :
		posb=self.posballe()
		if self.id_team==2:
			posg=Vector2D(GAME_WIDTH,GAME_HEIGHT/2)
		if self.id_team==1:
			posg=Vector2D(0,GAME_HEIGHT/2)
		return Vector2D((posb.x+posg.x)/2,(posb.y+posg.y)/2)

	def prox_balle(self) :
		posb=self.posballe()
		posj2=self.state.player_state(self.id_team%2+1,self.id_player).position
		distj1=self.distballe()
		distj2=math.hypot(posb.x-posj2.x,posb.y-posj2.y)
		if distj1>=distj2 :
			return True
		else :
			return False

	def balle_def(self) :
		posb=self.posballe()
		if self.id_team==1 and posb.x <= GAME_WIDTH/2 :
			return True
		elif self.id_team==2 and posb.x >= GAME_WIDTH/2 :
			return True
		else :
			return False
