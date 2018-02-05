from __future__ import absolute_import
from soccersimulator import ChallengeFonceurButeur, SoccerTeam,show_simu
from FonceurStrategy import FonceurStrategy

team = SoccerTeam("Team")
team.add("RedOne",FonceurStrategy())

challenge = ChallengeFonceurButeur(team,max_but=20)
show_simu(challenge)
print("temps moyen : ",challenge.stats_score, "\nliste des temps",challenge.resultats)
