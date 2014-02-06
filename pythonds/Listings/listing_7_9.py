def orderByAvail(n):
    resList = []
    for v in n.geConnections():
        if v.getColor() == 'white':
            c = 0
            for w in v.getConnections():
                if w.getColor() == 'white':
                    c = c + 1
            resList.append((c,v))
    resList.sort(key=lambda x: x[0])      return [y[1] for y in resList]   
