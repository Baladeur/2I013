from soccersimulator import Vector2D, SoccerState, SoccerAction
from soccersimulator import Simulation, SoccerTeam, Player, show_simu
from soccersimulator import Strategy
from soccersimulator import settings
from soccersimulator.settings import *
from modulesocc.strategies import *
import math


## Creation d'une equipe
red = SoccerTeam(name="Red")
blue = SoccerTeam(name="Blue")
red.add("Defenseur",ZigzagStrategy())
blue.add("Attaquant",FonceurStrategy())

#Creation d'une partie
simu = Simulation(red,blue)
#Jouer et afficher la partie
show_simu(simu)
