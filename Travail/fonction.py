from soccersimulator import Vector2D, SoccerState, SoccerAction
from soccersimulator import Simulation, SoccerTeam, Player, show_simu
from soccersimulator import Strategy
from soccersimulator import settings
from soccersimulator.settings import *
import math

class Etat(Object):
	def __init__(self,state):
		self.state=state
	def aller_balle(self,id_team,id_player): #retourne le vecteur entre le joueur et la balle
		return self.ball.position-self.player_state(id_team,id_player).position

	def vecteur_goal(self,id_team): #retourne le vecteur entre la balle et les cages
		if id_team==1:
			return Vector2D(GAME_WIDTH,GAME_HEIGHT/2)-self.ball.position
		if id_team==2:
			return Vector2D(0,GAME_HEIGHT/2)-self.ball.position
		return Vector2D(0,0)

	def dist(self,id_team,id_player): #retourne la distance (norme) entre le joueur et la balle
		return math.hypot(self.ball.position.x-self.player_state(id_team,id_player).position.x,self.ball.position.y-self.player_state(id_team,id_player).position.y)
