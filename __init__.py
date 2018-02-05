from __future__ import absolute_import
from ZigzagStrategy import ZigzagStrategy
from FonceurStrategy import FonceurStrategy
from RandomStrategy import RandomStrategy
from soccersimulator import SoccerTeam

def get_team(nb_players):
    myteam = SoccerTeam(name="MaTeam")
    if nb_players == 1:
        myteam.add("Joueur " ,ZigzagStrategy())
    if nb_players == 2:
	myteam.add("Joueur 1", RandomStrategy())
	myteam.add("Joueur 2", RandomStrategy())
    if nb_players == 4:
	myteam.add("Joueur 1",RandomStrategy())
	myteam.add("Joueur 2",RandomStrategy())
	myteam.add("Joueur 3",RandomStrategy())
	myteam.add("Joueur 4",RandomStrategy())
    return myteam	

def get_team_challenge(num):
	myteam = SoccerTeam(name="MaTeamChallenge")
	if num == 1:
		myteam.add("Joueur Chal "+str(num),BlueStrategy())
	return myteam