with open("AoC2023_02_data.txt", "r") as file:
    data = file.read()
    
data = data.split('\n')
ans1,ans2 = 0,0
d={'red':12,'green':13,'blue':14}

for line in data:
    game, hands = line.split(':')
    game = int(game.split(' ')[-1])
    hands = hands.split(';')
    ok = True
    d_min = {'red':0,'green':0,'blue':0}
    for hand in hands:
        cubes = hand.split(', ')
        for pair in cubes:
            n,c = pair.strip(' ').split(' ')
            n = int(n)
            if n>d[c]:
                ok = False
            d_min[c] = max(n,d_min[c])
    x = 1
    for n in d_min.values():
        x*=n
    ans2+=x
    if ok:
        ans1+=game
    
print(ans1,ans2)