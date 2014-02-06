def moveTower(height,fromPole, toPole, withPole):
	if height >= 1:
		moveTower(height-1,fromPole,withPole,toPole)  		moveDisk(fromPole,toPole)
		moveTower(height-1,withPole,toPole,fromPole)  
