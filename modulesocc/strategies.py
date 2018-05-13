from soccersimulator import Vector2D, SoccerState, SoccerAction
from soccersimulator import Simulation, SoccerTeam, Player, show_simu
from soccersimulator import Strategy
from soccersimulator import settings
from soccersimulator.settings import *
from .fonctions_strategies import *
from .actions_simples import *
from .etat import Etat
import math

class RandomStrategy(Strategy):
    def __init__(self):
        Strategy.__init__(self,"Random")
    def compute_strategy(self,state,id_team,id_player):
        return SoccerAction(Vector2D.create_random(-0.5,0.5),Vector2D.create_random(-0.5,0.5))

class FonceurStrategy(Strategy):
	def __init__(self):
		Strategy.__init__(self,"Fonceur Lambda")
	def compute_strategy(self,state,id_team,id_player):
		return fonceur_defaut(state,id_team,id_player, 4)

class DefenseStrategy(Strategy):
	def __init__(self):
		Strategy.__init__(self,"Defenseur")
	def compute_strategy(self,state,id_team,id_player):
		return defense(state,id_team,id_player, 3.5)

class AttaqueStrategy(Strategy):
	def __init__(self):
		Strategy.__init__(self,"Attaquant")
	def compute_strategy(self,state,id_team,id_player):
		return attaque(state,id_team,id_player, 5)
		
class Old_posdefStrategy(Strategy):
	def __init__(self):
		Strategy.__init__(self,"Defenseur")
	def compute_strategy(self,state,id_team,id_player):
		return arriere(state,id_team,id_player)

class Old_passeStrategy(Strategy):
	def __init__(self):
		Strategy.__init__(self,"Defenseur")
	def compute_strategy(self,state,id_team,id_player):
		return fairepasse(state,id_team,id_player,3.5)

class Old_pospasseStrategy(Strategy):
	def __init__(self):
		Strategy.__init__(self,"Attaquant")
	def compute_strategy(self,state,id_team,id_player):
		return recpasse(state,id_team,id_player)

class Old_dribbleStrategy(Strategy):
	def __init__(self):
		Strategy.__init__(self,"Attaquant")
	def compute_strategy(self,state,id_team,id_player):
		return dribble(state,id_team,id_player)

class Old_tirStrategy(Strategy):
	def __init__(self):
		Strategy.__init__(self,"Attaquant")
	def compute_strategy(self,state,id_team,id_player):
		return fonceur_defaut(state,id_team,id_player, 4)

class M_foncer_centreStrategy(Strategy):
	def __init__(self):
		Strategy.__init__(self,"Attaquant")
	def compute_strategy(self,state,id_team,id_player):
		return foncer_centre(state,id_team,id_player, 10)

class M_intercepte_centreStrategy(Strategy):
	def __init__(self):
		Strategy.__init__(self,"Attaquant")
	def compute_strategy(self,state,id_team,id_player):
		return intercepte_centre(state,id_team,id_player)

class M_tempo_centreStrategy(Strategy):
	def __init__(self):
		Strategy.__init__(self,"Attaquant")
	def compute_strategy(self,state,id_team,id_player):
		return tempo_centre(state,id_team,id_player, 10)

class M_feinteStrategy(Strategy):
	def __init__(self):
		Strategy.__init__(self,"Attaquant")
	def compute_strategy(self,state,id_team,id_player):
		return feinte(state,id_team,id_player)

class M_aller_goalStrategy(Strategy):
	def __init__(self):
		Strategy.__init__(self,"Aller goal")
	def compute_strategy(self,state,id_team,id_player):
		return aller_goal(state,id_team,id_player)

class M_aller_attaqueStrategy(Strategy):
	def __init__(self):
		Strategy.__init__(self,"Aller attaque")
	def compute_strategy(self,state,id_team,id_player):
		return aller_attaque(state,id_team,id_player, 20)

class M_aller_defenseStrategy(Strategy):
	def __init__(self):
		Strategy.__init__(self,"Aller defense")
	def compute_strategy(self,state,id_team,id_player):
		return aller_defense(state,id_team,id_player, 30)

class M_goalStrategy(Strategy):
	def __init__(self):
		Strategy.__init__(self,"Goal")
	def compute_strategy(self,state,id_team,id_player):
		return goal(state,id_team,id_player)

class M_tir_goalStrategy(Strategy):
	def __init__(self):
		Strategy.__init__(self,"Goal")
	def compute_strategy(self,state,id_team,id_player):
		return tir_goal(state,id_team,id_player,7)
		
class M_rec_passe_defStrategy(Strategy):
	def __init__(self):
		Strategy.__init__(self,"Goal")
	def compute_strategy(self,state,id_team,id_player):
		return rec_passe_def(state,id_team,id_player)
		
class M_rec_passe_atqStrategy(Strategy):
	def __init__(self):
		Strategy.__init__(self,"Goal")
	def compute_strategy(self,state,id_team,id_player):
		return rec_passe_atq(state,id_team,id_player)
		
class M_dribble_passe_atqStrategy(Strategy):
	def __init__(self):
		Strategy.__init__(self,"Goal")
	def compute_strategy(self,state,id_team,id_player):
		return dribble_passe(state,id_team,id_player)

class M_passe_atqStrategy(Strategy):
	def __init__(self):
		Strategy.__init__(self,"Goal")
	def compute_strategy(self,state,id_team,id_player):
		return passe_attaque(state,id_team,id_player,1.5)

class M_passe_atqStrategy(Strategy):
	def __init__(self):
		Strategy.__init__(self,"Goal")
	def compute_strategy(self,state,id_team,id_player):
		return passe_defense(state,id_team,id_player,1.5)

class M_goal_intercepteStrategy(Strategy):
	def __init__(self):
		Strategy.__init__(self,"Goal")
	def compute_strategy(self,state,id_team,id_player):
		return goal_intercepte(state,id_team,id_player)
		
class AttaqueNewStrategy(Strategy):
	def __init__(self):
		Strategy.__init__(self,"Goal")
	def compute_strategy(self,state,id_team,id_player):
		return attaque_new(state,id_team,id_player)