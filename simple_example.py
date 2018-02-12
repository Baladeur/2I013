from __future__ import absolute_import
from soccersimulator import Vector2D, SoccerState, SoccerAction
from soccersimulator import Simulation, SoccerTeam, Player, show_simu
from soccersimulator import Strategy
from soccersimulator import settings
from soccersimulator.settings import *
#import sys
#sys.path.insert(0, '/users/nfs/Etu1/3520421/2017-2018/2I013/git/modulesocc')
from modulesocc.strategies import *
import math

## Creation d'une equipe
red = SoccerTeam(name="Red")
blue = SoccerTeam(name="Blue")
red.add("Red One",ZigzagStrategy()) #Strategie qui ne fait rien
blue.add("Blue One",FonceurStrategy())   #Strategie aleatoire

#Creation d'une partie
simu = Simulation(red,blue)
#Jouer et afficher la partie
show_simu(simu)
