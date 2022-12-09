f = open("prova.txt", "r")
data = f.read()
data=data.split('\n\n')

dict = {}
for tile in data:
    tile = tile.split('\n')
    dict[int(tile[0][5:-1])]=tile[1:]

N = int((len(dict))**0.5)
puzzle = [ [0 for i in range(N)] for j in range(N)]
solution = []

def solve(dict,puz,already_used,r,c,solution): 
    if len(already_used) == len(dict):
        solution += [already_used]
        return puz

    for n,tile in dict.items():
        if n not in already_used:
            for possibility in poss(tile):
                if check(puz,r,c,possibility):
                    puz[r][c] = possibility
                    if c<N-1:
                        c1 = c+1
                        r1 = r
                    else:
                        r1 = r+1
                        c1 = 0

                    solve(dict,puz,already_used+[n],r1,c1,solution)


def solve2(dict,puz,already_used,r,c,solution): 
    if len(already_used) == len(dict):
        solution += [already_used]
        return puz

    for n,tile in dict.items():
        if n not in already_used:
            for possibility in poss(tile):
                if check(puz,r,c,possibility):
                    print(type(puz))
                    print(puz)
                    puz[r][c] = possibility
                    if c<N-1:
                        c1 = c+1
                        r1 = r
                    else:
                        r1 = r+1
                        c1 = 0

                    return solve(dict,puz,already_used+[n],r1,c1,solution)
                return puz
        return puz

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
        to_add += [flip(x)]
    p = p+to_add
    return p

print(solve(dict,puzzle,[],0,0,solution))

        