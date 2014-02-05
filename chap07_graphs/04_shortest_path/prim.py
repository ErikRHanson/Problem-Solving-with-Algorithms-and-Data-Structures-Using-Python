from Vertex import Vertex
from Graph import Graph
from PriorityQueue import PriorityQueue

def prim(G,start):
	pr = PriorityQueue()
	for v in G:
		v.setDistance(sys.maxsize)
		v.setPred(None)
	start.setDistance(0)
	pq.buildHeap([(v.getDistance(),v) for v in G])
	while not pq.isEmpty():
		currentVert = pq.delMin()
		for nextVert in currentVert.getConnections():
			newCost = currentVert.getWeight(nextVert) + currentVert.getDistance()
			if v in pq and newCost<nextVert.getDistance():
				nextVert.setPred(currentVert)
				nextVert.setDistance(newCost)
				pq.decreaseKey(newVert,newCost)


	