from soccersimulator import SoccerAction,Vector2D,settings ,SoccerTeam,Billard,show_simu,Strategy
import math

class Etat(object):
	def __init__(self,state) :
		self.state = state
	
	#Position de la balle
	def posballe(self) 	:
		return self.state.ball.position

	#Vitesse de la balle
	def spballe(self) 	:
		return self.state.ball.vitesse

	#Position du joueur
	def posjoueur(self) 	:
		return self.state.player_state(1,0).position

	#vitesse du joueur
	def posjoueur(self) 	:
		return self.state.player_state(1,0).position

	#Position d'une balle
	def posballs(self,nb) 	:
		return self.state.balls[nb].position

	#Vitesse d'une balle
	def spballs(self,nb) 	:
		return self.state.balls[nb].vitesse

	#Distance entre deux positions
	def dist(self,pos1,pos2)	:
		return math.hypot(pos1.x-pos2.x,pos1.y-pos2.y)
