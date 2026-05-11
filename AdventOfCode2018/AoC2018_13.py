from dataclasses import dataclass

for file in ["AoC2018_13_test.txt","AoC2018_13_data.txt"]:

    with open(file, "r") as f:
        data = f.read()
        
    @dataclass
    class Cart:
        r: int
        c: int
        d: int
        turn: int = 0
        alive: bool = True
        
    def parse_input(filename):
        with open(filename) as f:
            data = f.read().splitlines()
    
        carts = []
        grid = [list(line) for line in data]
    
        for r, row in enumerate(grid):
            for c, ch in enumerate(row):
                if ch in '^v<>':
                    direction = {'>':0, 'v':1, '<':2, '^':3}[ch]
                    carts.append(Cart(r, c, direction))
                    row[c] = '|' if ch in '^v' else '-'

        return grid, carts
                
    def move(cart, grid):
        tile = grid[cart.r][cart.c]
    
        if tile == '+':
            if cart.turn == 0:        # turn left
                cart.d = (cart.d - 1) % 4
            elif cart.turn == 2:      # turn right
                cart.d = (cart.d + 1) % 4
            # turn_state == 1 → straight (no change)
            cart.turn = (cart.turn + 1) % 3
    
        elif tile in CURVE:
            cart.d = CURVE[tile][cart.d]
    
        dr, dc = DIR[cart.d]
        cart.r += dr
        cart.c += dc
                
    def tick(grid, carts):
        carts.sort(key=lambda x: (x.r, x.c))
        occupied = {(cart.r, cart.c): cart for cart in carts if cart.alive}
        first_crash = None
    
        for cart in carts:
            if not cart.alive:
                continue
    
            del occupied[(cart.r, cart.c)]
            move(cart, grid)
            pos = (cart.r, cart.c)
    
            if pos in occupied:
                other = occupied[pos]
                cart.alive = other.alive = False
                del occupied[pos]
                if not first_crash:
                    first_crash = (cart.c, cart.r)   # x,y format
            else:
                occupied[pos] = cart
    
        alive_carts = [c for c in carts if c.alive]
        survivor = None
        if len(alive_carts) == 1:
            survivor = (alive_carts[0].c, alive_carts[0].r)
        return first_crash, survivor
                
        
    def output(grid, carts):
        for r in range(len(grid)):
            row = list(grid[r])
            for cart in carts:
                if cart.alive and cart.r == r:
                    row[cart.c] = DIR_symbols[cart.d]
            print(''.join(row))
        print()
        
    ans = [0,0]
    DIR = ((0,1),(1,0),(0,-1),(-1,0))
    DIR_symbols = {0:'>',1:'v',2:'<',3:'^'}
    CURVE = {
    '/':  {0: 3, 1: 2, 2: 1, 3: 0},
    '\\': {0: 1, 1: 0, 2: 3, 3: 2}
    }
    grid, carts = parse_input(file)
    first_crash = None
    final_survivor = None

    while not final_survivor:
        fc, survivor = tick(grid, carts)
        if fc and not first_crash:
            first_crash = fc
        if survivor:
            final_survivor = survivor

    print("Part 1 - First crash:", f"{first_crash[0]},{first_crash[1]}")
    print("Part 2 - Last cart:", f"{final_survivor[0]},{final_survivor[1]}")
        