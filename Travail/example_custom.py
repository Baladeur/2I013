from soccersimulator import Vector2D, SoccerState, SoccerAction
from soccersimulator import Simulation, SoccerTeam, Player, show_simu
from soccersimulator import Strategy
from soccersimulator import settings
from soccersimulator.settings import *
import math


## Strategie aleatoire
class RandomStrategy(Strategy):
    def __init__(self):
        Strategy.__init__(self,"Random")
    def compute_strategy(self,state,id_team,id_player):
        return SoccerAction(Vector2D.create_random(-0.5,0.5),Vector2D.create_random(-0.5,0.5))


class RedStrategy(Strategy):
	def __init__(self):
		Strategy.__init__(self,"Red")
	def compute_strategy(self,state,id_team,id_player):
		balle=state.ball.position
		joueur=state.player_state(id_team,id_player).position
		direction_balle=balle-joueur
		direction_balle.norm=1
		distance=math.hypot(balle.x-joueur.x,balle.y-joueur.y)
		if id_team==1:
			direction_goal=Vector2D(GAME_WIDTH,GAME_HEIGHT/2)-balle
		if id_team==2:
			direction_goal=Vector2D(0,GAME_HEIGHT/2)-balle
		direction_goal.norm=2
		if distance <= PLAYER_RADIUS+BALL_RADIUS:
			return SoccerAction(direction_balle,direction_goal)
		else:
			return SoccerAction(direction_balle)

class BlueStrategy(Strategy):
	def __init__(self):
		Strategy.__init__(self,"Blue")
	def compute_strategy(self,state,id_team,id_player):
		balle=state.ball.position
		speed=state.ball.vitesse
		joueur=state.player_state(id_team,id_player).position
		joueur2=state.player_state((id_team)%2+1,id_player).position
		direction_balle=balle-joueur
		direction_balle.norm=1
		distance=math.hypot(balle.x-joueur.x,balle.y-joueur.y)
		if id_team==1:
			direction_goal=Vector2D(GAME_WIDTH,GAME_HEIGHT/2)-balle
		if id_team==2:
			direction_goal=Vector2D(0,GAME_HEIGHT/2)-balle
		
		if speed.x>0:
			anticipe=balle.y+(direction_goal.x/speed.x)*speed.y
			if anticipe>=GAME_HEIGHT/2-GAME_GOAL_HEIGHT and anticipe<=GAME_HEIGHT/+GAME_GOAL_HEIGHT:
				if balle.y >=GAME_HEIGHT/2:
					direction_goal.angle += math.radians(30)
				if balle.y <GAME_HEIGHT/2:
					direction_goal.angle -= math.radians(30)
		direction_goal.norm=2
		if distance <= PLAYER_RADIUS+BALL_RADIUS:
			return SoccerAction(direction_balle,direction_goal)
		else:
			return SoccerAction(direction_balle)


## Creation d'une equipe
red = SoccerTeam(name="Red")
blue = SoccerTeam(name="Blue")
red.add("Red One",BlueStrategy()) #Strategie qui ne fait rien
blue.add("Blue One",RandomStrategy2())   #Strategie aleatoire

#Creation d'une partie
simu = Simulation(red,blue)
#Jouer et afficher la partie
show_simu(simu)
