def buildAndDisplay():
    im = Image.open('bubbles.jpg')
    w,h = im.size
    ot = OctTree()
    for row in range(0,h):                  for col in range(0,w):
            r,g,b = im.getpixel((col,row))
            ot.insert(r,g,b)       
    ot.reduce(256)  # reduce to 256 colors  
    for row in range(0,h):
        for col in range(0,w):
            r,g,b = im.getpixel((col,row))
            nr,ng,nb = ot.find(r,g,b)              im.putpixel((col,row),(nr,ng,nb))  # replace pixel with new quantized values

    im.show()    
