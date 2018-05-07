from soccersimulator import SoccerAction,Vector2D,settings ,SoccerTeam,Billard,show_simu,Strategy
from tmesolo1.actions_simples import *
from tmesolo1.etat import *
import math

class FonceurLent(Strategy):
	def __init__(self):
		super(FonceurLent,self).__init__("fonceur")
	def compute_strategy(self,state,idteam,idplayer):
		ball = state.ball
		me = state.player_state(1,0)
		oth = state.balls[0]
		shoot = (oth.position-ball.position)*100
		e=Etat(state)
        #if (me.position.distance(ball.position)<(settings.BALL_RADIUS+settings.PLAYER_RADIUS)) and  me.vitesse.norm<0.5:
		#return SoccerAction(shoot=shoot)
		#acc = ball.position-me.position
		#if acc.norm<5:
		#acc.norm=0.1
		#return SoccerAction(acceleration=acc)
		if (me.position.distance(ball.position)<(settings.BALL_RADIUS+settings.PLAYER_RADIUS)) and  me.vitesse.norm<0.5:
			return SoccerAction(shootb(e,0))
		elif (me.position.distance(ball.position)<(settings.BALL_RADIUS+settings.PLAYER_RADIUS)) and  me.vitesse.norm>0.5:
			print("ralenti")
			return SoccerAction(ralenti(e,0))
		else :
			return SoccerAction(dirpos(e,1,pos_tir(e,0)))

myt = SoccerTeam("prof")
myt.add("N",FonceurLent())
b = Billard(myt,type_game=0)
show_simu(b)

