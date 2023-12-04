with open("AoC2020_17_data.txt", "r") as file:
    data = file.read()
data=data.split('\n')

X,Y = len(data),len(data[0])

def active(G,i,j,k,h):
    n = 0
    for ii in [i-1,i,i+1]:
        for jj in [j-1,j,j+1]:
            for kk in [k-1,k,k+1]:
                for hh in [h-1,h,h+1]:
                    if not (hh==h and ii==i and jj==j and kk==k) and (ii,jj,kk,hh) in G:    
                        n += 1
    return n
            
def iteration(G,part):
    to_occupy,to_free = set(),set()
    for (i,j,k,h) in G:
        if part==1 and h!=0:
            continue
        if not active(G,i,j,k,h) in [2,3]:
            to_free.add((i,j,k,h))
        for ii in [i-1,i,i+1]:
            for jj in [j-1,j,j+1]:
                for kk in [k-1,k,k+1]:
                    if part==1:
                        if (ii,jj,kk,h) not in G and active(G,ii,jj,kk,h)==3:
                            to_occupy.add((ii,jj,kk,h))
                    else:
                        for hh in [h-1,h,h+1]:
                            if (ii,jj,kk,hh) not in G and active(G,ii,jj,kk,hh)==3:
                                to_occupy.add((ii,jj,kk,hh))
    for (i,j,k,h) in to_occupy:
        G.add((i,j,k,h))
    for (i,j,k,h) in to_free:
        G.remove((i,j,k,h))
    return G

for part in [1,2]:
    G = set()
    for x in range(X):
        for y in range(Y):
            if data[x][y]=='#':
                G.add((x,y,0,0))
    for k in range(6):
        G=iteration(G,part)
    print(len(G))