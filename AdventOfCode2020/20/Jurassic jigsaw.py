f = open("data.txt", "r")
data = f.read()
data=data.split('\n\n')

dict = {}

for tile in data:
    tile = tile.split('\n')
    dict[int(tile[0][5:-1])]=tile[1:]

def borders(tile):
    up,down = tile[0],tile[-1]
    left,right = '',''
    for line in tile:
        right = right+line[-1]
        left = left+line[0]
    
    return [up,right,down[::-1],left[::-1]]

def totborders(tile):
    b = borders(tile)
    return [b[0],b[0][::-1],b[1],b[1][::-1],b[2],b[2][::-1],b[3],b[3][::-1]] 

product=1

for n,tile in dict.items():
    pairs = 0
    for border in borders(tile):
        for m,tile1 in dict.items():
            if m!=n:
                b1 = totborders(tile1)
                if border in b1:
                    pairs=pairs+1
                    break
    if pairs==2:
        product=product*n
        
print(product)