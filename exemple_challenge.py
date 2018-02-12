from __future__ import absolute_import
from soccersimulator import ChallengeFonceurButeur, SoccerTeam,show_simu
import sys
sys.path.insert(0, '/users/nfs/Etu1/3520421/2017-2018/2I013/git/modulesocc')
from strategies import *

team = SoccerTeam("Team")
team.add("RedOne",FonceurStrategy())

challenge = ChallengeFonceurButeur(team,max_but=20)
show_simu(challenge)
print("temps moyen : ",challenge.stats_score, "\nliste des temps",challenge.resultats)
