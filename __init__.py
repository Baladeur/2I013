from .modulesocc.strategies import *
from soccersimulator import SoccerTeam

def get_team(nb_players):
	myteam = SoccerTeam(name="Started from the bottom")
	if nb_players == 1:
		myteam.add("Joueur" ,AttaqueStrategy())
	if nb_players == 2:
		myteam.add("Defenseur", DefenseStrategy())
		myteam.add("Attaquant", AttaqueStrategy())
	if nb_players == 4:
		myteam.add("Attaquant",AttaqueStrategy())
		myteam.add("Support",AttaqueStrategy())
		myteam.add("Defense",DefenseStrategy())
		myteam.add("Goal",M_goal_intercepteStrategy())
	return myteam	

def get_team_challenge(num):
	myteam = SoccerTeam(name="MaTeamChallenge")
	if num == 1:
		myteam.add("Joueur Chal "+str(num),BlueStrategy())
	return myteam
