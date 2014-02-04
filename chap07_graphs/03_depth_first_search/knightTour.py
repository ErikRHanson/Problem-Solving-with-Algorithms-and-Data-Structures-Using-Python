from Graph import Graph
from Vertex import Vertex

def knightTour(n,path,u,limit):
	u.setColor('gray')
	path.append(u)
	if n < limit:
		nbrList = list(u.getConnections())
		i = 0
		done = False
		while i < len(nbrList) and not done:
			if nbrList[i].getColor() == 'white':
				done = knightTour(n+1, path, nbrList[i], limit)
			i = i + 1
		if not done:	# prepare to backtrack
			path.pop()
			u.setColor('white')
	else:
		done = True
	return done


def knightTour2(n,path,u,limit):
	u.setColor('gray')
	path.append(u)
	if n < limit:
		nbrList = orderByAvail(u)
		i = 0
		done = False
		while i < len(nbrList) and not done:
			if nbrList[i].getColor() == 'white':
				done = knightTour(n+1, path, nbrList[i], limit)
			i = i + 1
		if not done:	# prepare to backtrack
			path.pop()
			u.setColor('white')
	else:
		done = True
	return done


def orderByAvail(n):
	resList = []
	for v in n.getConections():
		if v.getColor() == 'white':
			c = 0
			for w in v.getConnections():
				if w.getColor() == 'white':
					c = c + 1
			resList.append((c,v))
	resList.sort(key=lambda x: x[0])
	return [y[1] for y in resList]
