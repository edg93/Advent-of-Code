from collections import defaultdict

data = 312051
ans = [0,0]

n = 1
while n**2<data:
    n +=2
    
rest = data-(n-2)**2
pos = rest%(n-1)
ans[0] = (n-1)//2 + (abs(pos-(n-1)//2))

def part2(data):
    grid = defaultdict(int)
    grid[(0, 0)] = 1

    x = y = 0
    step = 1

    directions = [(1,0), (0,1), (-1,0), (0,-1)]

    def neighbor_sum(x, y):
        return sum(
            grid[(x+dx, y+dy)]
            for dx in (-1, 0, 1)
            for dy in (-1, 0, 1)
            if not (dx == dy == 0)
        )

    while True:
        for d in range(4):
            dx, dy = directions[d]
            for _ in range(step):
                x += dx
                y += dy

                val = neighbor_sum(x, y)
                grid[(x, y)] = val

                if val > data:
                    return val

            if d % 2 == 1:
                step += 1
ans[1] = part2(data)
print(ans)