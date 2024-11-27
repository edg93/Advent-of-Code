with open("AoC2023_17_test.txt", "r") as file:
    data = file.read()

data = data.split('\n')
R,C = len(data),len(data[0])

ans1,ans2=0,0
DIR = ((1,0),(-1,0),(0,1),(0,-1))


to_process = set()
d_cost = {}

costs = [[None for x in line] for line in data]
costs[-1][-1]=data[-1][-1]


def moves(r,c):
    moves = set()
    for mov in DIR:
        r1 = r + mov[0]
        c1 = c + mov[1]
        if 0<=r1<R and 0<=c1<C:
            moves.add((r1,c1))
    return moves

        