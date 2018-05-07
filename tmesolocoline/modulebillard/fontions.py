#Booléen indiquant si la balle va vers les cages
	def trajectoire_goal(self,id_t) :
		posb=state.ball.position
		posg=pos_cages(id_t)
		speed=state.ball.vitesse
		distx=posg.x-posb.x
		k=distx/speed.x
		anticipe_goal=posb+speed*k
		if (anticipe_goal.y <= GAME_HEIGHT/2+5) and (anticipe_goal.y >= GAME_HEIGHT/2-5) :
			return True
		else :
			return False

#Position entre la balle et les cages
def pos_cages(id_t) :
	v_ball=state.ball.vitesse
	pos_ball=state.ball.position
	pos_cages
	if id_t==2:
		pos_cages = Vector2D(GAME_WIDTH,GAME_HEIGHT/2)
	if id_t==1:
		pos_cages = Vector2D(0,GAME_HEIGHT/2)
	distx=pos_cages.x-pos_ball.x #calcul de la distance en x séparant la balle des cages
	if v_ball.x/distx >= 0 and b_ball.x >0 :
		k=distx/v_ball.x 
		arriv=pos_ball.y+k*v_ball.y #calcul du point d'arrivée en y de la balle dans les cages
		return Vector2D((pos_ball.x*(0.5)+pos_cages.x*0.5),(pos_ball.y*(0.5)+arriv*0.5))
	else :
		return Vector2D(pos_ball.x,pos_ball.y)



def can_shoot(vitesse):

		return true

def angle_tir(oth): #retourne l'angle nécessaire pour viser les goals
	me = state.player_state(1,0)
	ball = state.ball
	i = 0
	v_oth = oth.vitesse
	while not (can_shoot(v_oth)):
		i = i+1
		v_oth .angle += 1
	return i

def dirballe(idt, idp,norme) :
	vect = state.ball.position-state.player_state(idt, idp).position
	vect.norm = norme
	return vect

def dirpos(id_t_id_p,norme,pos):
	vect = pos-state.player_state(id_t, id_p)).position
	vect.norm = norme
	return vect

def dirgoal(etat,norme) :
	vect=Vector2D(0,0)
	posg=pos_cages
	vect=posg-state.ball.position
	vect.norm=norme
	return vect