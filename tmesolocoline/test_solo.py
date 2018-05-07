from soccersimulator import SoccerAction,Vector2D,settings ,SoccerTeam,Billard,show_simu,Strategy
from modulebillard.strategies import MyStrategy

myt = SoccerTeam("Coline")
myt.add("C",MyStrategy())
b = Billard(myt,type_game=-1)
show_simu(b)
