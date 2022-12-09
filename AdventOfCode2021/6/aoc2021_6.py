"Day 6 of AOC2021"
with open("data.txt", "r") as file:
    data = file.read()
data=data.split(',')
data = [int(x) for x in data]
N=256
fishes = [0 for x in range(9)]

for fish in data:
    fishes[fish] += 1


def evolve(fish_list):
    "one step evolution of the fish_list"
    new_list = fish_list[1:]+[fish_list[0]]
    new_list[6] += fish_list[0]
    return new_list

for x in range(N):
    fishes = evolve(fishes)

print(sum(fishes))
