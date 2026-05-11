from collections import deque
#419 players; last marble is worth 71052 points

n_players = 419
last_marble = 7105200
marble = 1
ans = [0,0]

players = [0 for _ in range(n_players)]

i = 0

marbles = deque([0])

for marble in range(1,last_marble+1):
    player = marble % n_players
    if marble%23 == 0:
        marbles.rotate(7)
        players[player]+=marble + marbles.pop()
        marbles.rotate(-1)
    else:
        marbles.rotate(-1)
        marbles.append(marble)
    if marble == 71052:
        ans[0] = max(players)

ans[1]=max(players)
print(ans)