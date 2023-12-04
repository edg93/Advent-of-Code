from copy import copy

with open("AoC2020_20_data.txt", "r") as file:
    data = file.read()
data=data.split('\n\n')

tiles = {}

for tile in data:
    tile = tile.split('\n')
    tiles[int(tile[0][5:-1])]=tile[1:]

def borders(tile):
    up,down = tile[0],tile[-1]
    left,right = '',''
    for line in tile:
        right += line[-1]
        left += line[0]
    
    return [up,right,down[::-1],left[::-1]]

def totborders(tile):
    u,r,d,l = borders(tile)
    return [u,u[::-1],r,r[::-1],d,d[::-1],l,l[::-1]] 

def check_neighbours(tile,tile1):
    for b in totborders(tile):
        if b in totborders(tile1):
            return True

def find_neighbours(n):
    tile = tiles[n]
    neighbours = set()
    for n1,tile1 in tiles.items():
        if n1!=n and check_neighbours(tile,tile1):
            neighbours.add(n1)
    return neighbours

def check(puz,r,c,tile):
    if r>0:
        if tile[0]!=puz[r-1][c][-1]:
            return False
    if c>0:
        if left_border(tile)!=right_border(puz[r][c-1]):
            return False
    return True   
        
def left_border(tile):
    left = ''
    for line in tile:
        left += line[0]
    return left

def right_border(tile):
    right = ''
    for line in tile:
        right += line[-1]
    return right

def rotate(tile):
    rotated = [[0 for i in range(len(tile))] for j in range(len(tile))]
    for r in range(len(tile)):
        for c in range(len(tile)):
            rotated[r][c]=tile[c][len(tile)-r-1]
    for r in range(len(rotated)):
        rotated[r]=''.join(rotated[r])
    return rotated
    
def flip(tile):
    flipped = []
    for line in tile:
        flipped += [line[::-1]] 
    return flipped 
    
def poss(tile):
    p = [tile,rotate(tile),rotate(rotate(tile)),rotate(rotate(rotate(tile)))]
    to_add = []
    for x in p:
        to_add.append(flip(x))
    return p + to_add

def solve(tiles,puz,already_used,orientations,r,c,solution): 
    if len(already_used) == len(tiles):
        if already_used not in solution:
            solution += [(already_used,orientations)]
    if r==c==0:
        list_tiles = tiles.keys()
    elif c==0:
        list_tiles = neighbours[already_used[-N]]
    else:
        list_tiles = neighbours[already_used[-1]]
    for n in list_tiles:
        tile = tiles[n]
        if n not in already_used:
            for orientation,tile1 in enumerate(poss(tile)):
                if check(puz,r,c,tile1):
                    puz1 = copy(puz)
                    puz1[r][c] = tile1
                    if c<N-1:
                        solve(tiles,puz1,already_used+[n],orientations+[orientation],r,c+1,solution)
                    else:
                        solve(tiles,puz1,already_used+[n],orientations+[orientation],r+1,0,solution)

neighbours={}
ans1=1

for n,tile in tiles.items():
    neighbours[n]=find_neighbours(n)
    if len(neighbours[n])==2:
        ans1*=n
        
print(ans1)

N = int((len(tiles))**0.5)
puzzle = [[0 for i in range(N)] for j in range(N)]
solution = []
                        
solve(tiles,puzzle,[],[],0,0,solution)
puzzle = [ [0 for i in range(N)] for j in range(N)]

n_tiles,orientations = solution[0]
l = int(len(n_tiles)**(1/2))

for n,n_tile in enumerate(n_tiles):
    tile = tiles[n_tile] 
    orientation = orientations[n]
    tile = poss(tile)[orientation]
    puzzle[n//N][n%N]=tile
    
image = []
for line in puzzle:
    for r in range(1,len(line[0])-1):
        new_r = ''
        for tile in line:
            new_r += tile[r][1:-1]
        image.append(new_r)
        
monster = set([(0,18),(1,0),(1,5),(1,6),(1,11),(1,12),(1,17),(1,18),(1,19),(2,1),(2,4),(2,7),(2,10),(2,13),(2,16)])

M=0

for r in range(len(image)):
    for c in range(len(image[0])):
        if image[r][c]=='#':
            M+=1

for img in poss(image):
    pixels = set()
    for r0 in range(len(image)-2):
        for c0 in range(len(image[0])-19):
            for r,c in monster:
                ok = True
                if img[r0+r][c0+c]!='#':
                    ok = False
                    break
            if ok:
                for r,c in monster:
                    pixels.add((r0+r,c0+c))
    
    if len(pixels)!=0:
        print(M-len(pixels))
        break