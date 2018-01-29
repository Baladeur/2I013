from soccersimulator import SoccerTeam, Simulation, show_simu, Strategy
from strategies  import RandomStrategy
from strategies  import BlueStrategy
from strategies  import RedStrategy


## Creation d'une equipe
Red = SoccerTeam(name="Red")
Blue = SoccerTeam(name="Blue")
red.add("RedOne",BlueStrategy()) #Strategie qui ne fait rien
blue.add("BlueOne",RandomStrategy())   #Strategie aleatoire

#Creation d'une partie
simu = Simulation(pyteam,thon)
#Jouer et afficher la partie
show_simu(simu)
