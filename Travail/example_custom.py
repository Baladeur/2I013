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
		direction_balle.norm=0.06
		direction_goal=Vector2D.create_random(-0.5,0.5)
		if id_team==0:
			direction_goal=Vector2D(150,45)-balle
		if id_team==0:
			direction_goal=Vector2D(0,45)-balle
		direction_goal.norm=0.5
		return SoccerAction(direction_balle,direction_goal)

class BlueStrategy(Strategy):
	def __init__(self):
		Strategy.__init__(self,"Blue")
	def compute_strategy(self,state,id_team,id_player):
		return SoccerAction(Vector2D(0,0,-3.14/2,0.04),Vector2D(-1.0,0.0))

## Creation d'une equipe
red = SoccerTeam(name="Red")
blue = SoccerTeam(name="Blue")
red.add("Red One",RedStrategy()) #Strategie qui ne fait rien
blue.add("Blue One",RedStrategy())   #Strategie aleatoire

#Creation d'une partie
simu = Simulation(red,blue)
#Jouer et afficher la partie
show_simu(simu)
