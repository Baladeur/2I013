from __future__ import absolute_import
from soccersimulator import Vector2D, SoccerState, SoccerAction
from soccersimulator import Simulation, SoccerTeam, Player, show_simu
from soccersimulator import Strategy
from soccersimulator import settings
from soccersimulator.settings import *
from fonctions_strategies import *
from actions_simples import *
from etat import Etat
import math

class RandomStrategy(Strategy):
    def __init__(self):
        Strategy.__init__(self,"Random")
    def compute_strategy(self,state,id_team,id_player):
        return SoccerAction(Vector2D.create_random(-0.5,0.5),Vector2D.create_random(-0.5,0.5))

class ZigzagStrategy(Strategy):
	def __init__(self):
		Strategy.__init__(self,"Zigzag")
	def compute_strategy(self,state,id_team,id_player):
		e=Etat(state,id_team,id_player)
		dist=e.distballe()
		if (dist <= PLAYER_RADIUS+BALL_RADIUS):
			return SoccerAction(dirballe(e,1),deviation(e,2))
		else:
			return SoccerAction(dirballe(e,1))

class FonceurStrategy(Strategy):
	def __init__(self):
		Strategy.__init__(self,"Zigzag")
	def compute_strategy(self,state,id_team,id_player):
		e=Etat(state,id_team,id_player)
		dist=e.distballe()
		if (dist <= PLAYER_RADIUS+BALL_RADIUS):
			return SoccerAction(dirballe(e,2),dirgoal(e,3.65))
		else:
			return SoccerAction(dirballe(e,2))

"""class DefenseStrategy(Strategy):
	def __init__(self):
		Strategy.__init__(self,"Defense")
	def compute_strategy(self,state,id_team,id_player):
		e=Etat(state,id_team,id_player)
		return SoccerAction()"""