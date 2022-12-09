"Day 6 of AOC2022"
with open("AoC2022_06_data.txt", "r") as file:
    data = file.read()

def find_marker(s,n):
    for i in range(len(s)-n):
        if len({x for x in data[i:i+n]})==n:
            print(i+n)
            break

n1,n2=4,14

find_marker(data,n1)
find_marker(data,n2)