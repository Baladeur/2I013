from soccersimulator import Vector2D, SoccerState, SoccerAction
from soccersimulator import Simulation, SoccerTeam, Player, show_simu
from soccersimulator import Strategy
from soccersimulator import settings
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
		return SoccerAction(Vector2D(1.0,0.0),Vector2D(1.0,0.0))

class BlueStrategy(Strategy):
	def __init__(self):
		Strategy.__init__(self,"Blue")
	def compute_strategy(self,state,id_team,id_player):
		return SoccerAction(Vector2D(-1.0,0.0),Vector2D(-1.0,0.0))

## Creation d'une equipe
red = SoccerTeam(name="Red")
blue = SoccerTeam(name="Blue")
red.add("Red One",RedStrategy()) #Strategie qui ne fait rien
blue.add("Blue One",BlueStrategy())   #Strategie aleatoire

#Creation d'une partie
simu = Simulation(red,blue)
#Jouer et afficher la partie
show_simu(simu)
