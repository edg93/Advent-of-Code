from PIL import Image
import numpy as np

with open("AoC2022_14_data.txt", "r") as file:
    data = file.read()
data=data.strip().split('\n')

def translate(c,C):
    return c-C[0]

def show(G):
    for line in G:
        print(''.join(line))
        
def count(G):
    counter = 0
    for line in G:
        counter += line.count('o')
    return counter

def move(G,p,R,C):
    r,c,x = p
    r = r+1
    if r>=R[1]:
        return r,c,False
    elif c+1>=C[1]:
        return r,c+1,False
    elif c==0:
        return r,c-1,False
    elif G[r+1][translate(c,C)]==empty:
        return r,c,True
    elif G[r+1][translate(c-1,C)]==empty:
        return r,c-1,True
    elif  G[r+1][translate(c+1,C)]==empty:
        return r,c+1,True
    else:
        return r,c,False
    
def insert(G,R,C,px):
    p = (-1,500,True)
    while p[2]:
        p = move(G,p,R,C)
    if R[0]<=p[0]<R[1] and C[0]<=p[1]<C[1]:
        G[p[0]][translate(p[1],C)] = 'o'
        px[p[0]][translate(p[1],C)]=[255,0,0]
        return G,True,px
    else:
        return G,False,px

R,C = [0,0],[500,500]
empty = ' '

for i in range(len(data)):
    data[i] = [x.split(',') for x in data[i].split(' -> ')]
    data[i] = [(int(a),int(b)) for [a,b] in data[i]]
    for pair in data[i]:
        C[0] = min(C[0],pair[0])
        C[1] = max(C[1],pair[0])
        R[1] = max(R[1],pair[1])
        
extension = R[1]+3
R1 = [0,R[1]+2]
C1 = [500-extension,500+extension]

G = [[empty for _ in range(C[1]-C[0]+1)] for _ in range(R[1]+1)]
G1 = [[empty for _ in range(C1[1]-C1[0]+1)] for _ in range(R1[1]+1)]
G1[-1]=['#'for _ in range(C1[1]-C1[0]+1)]

video_on = True

for GG,RR,CC,part in [(G,R,C,1),(G1,R1,C1,2)]:
    counter=1
    px = [[[255,255,255] for _ in range(CC[1]-CC[0]+1)] for _ in range(RR[1]+1)]
    px = np.array(px,dtype=np.uint8)
    
    for line in data:
        for i in range(len(line)-1):
            for r in range(min(line[i][1],line[i+1][1]),max(line[i][1],line[i+1][1])+1):
                for c in range(min(line[i][0],line[i+1][0]),max(line[i][0],line[i+1][0])+1):
                    GG[r][translate(c,CC)]='#'
                    px[r][translate(c,CC)]=[0,0,0]
    added = True
    
    while added:
        GG,added,px = insert(GG,RR,CC,px)      
        if video_on:
            im = Image.fromarray(px)
            width,height = im.size
            im = im.resize((width*5,height*5))
            im.save('images/images' + str(part) + '/' + str(counter) + '.png')
        counter += 1
        if GG[0][translate(500,CC)] == 'o':
            break

    print(count(GG))

#"ffmpeg -f image2 -r 1/5 -i ./images/%01d.png -vcodec mpeg4 -y video.mp4" da terminale per creare il video