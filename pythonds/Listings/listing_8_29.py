def mismatchLinks(pattern):
    augPattern = "0"+pattern
    links = {}
    links[1] = 0
    for k in range(2,len(augPattern)):
        s = links[k-1]
        stop = False
        while s>=1 and not stop:
            if augPattern[s] == augPattern[k-1]:
                stop = True
            else:
                s = links[s]
        links[k] = s+1
    return links
