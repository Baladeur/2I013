from soccersimulator import SoccerAction,Vector2D,settings ,SoccerTeam,Billard,show_simu,Strategy

class MyStrategy(Strategy):
	def __init__(self):
		super(MyStrategy,self).__init__("mystrat")
		def compute_strategy(self,state,idteam,idplayer):
			ball = state.ball
			me = state.player_state(1,0)
			oth = state.balls[0]
			shoot = (oth.position-ball.position)*100
			shoot.norm = 5
			pos = pos_cages(state.player_state.idteam)
			print("test");
			if (ball.position == pso_cages):
				return SoccerAction(shoot=shoot)
			acc = ball.position-me.position
			if acc.norm<5:
				acc.norm=5
			return SoccerAction(acceleration=acc)
