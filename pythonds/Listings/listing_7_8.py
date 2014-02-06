from pythonds.graphs import Graph, Vertex
def knightTour(n,path,u,limit): 
        u.setColor('gray')
        path.append(u)
        if n < limit:
            nbrList = list(u.getConnections())              i = 0
            done = False
            while i < len(nbrList) and not done:
                if nbrList[i].getColor() == 'white':
                    done = knightTour(n+1,                                            path, 
                                      nbrList[i],
                                      limit)
                i = i + 1    
            if not done:  # prepare to backtrack
                path.pop()
                u.setColor('white')
        else:
            done = True
        return done
