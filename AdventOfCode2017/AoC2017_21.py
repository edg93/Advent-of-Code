with open("AoC2017_21_data.txt", "r") as f:
    data = f.read()
    
data = data.splitlines()
ans = [0,0]

def parse_rules(lines):
    rules = {}

    def rotate(pattern):
        """Rotate a square pattern 90° clockwise"""
        rows = pattern.split('/')
        size = len(rows)
        return '/'.join(''.join(rows[size-1-j][i] for j in range(size)) for i in range(size))

    def flip(pattern):
        """Flip a square pattern horizontally"""
        return '/'.join(row[::-1] for row in pattern.split('/'))

    for line in lines:
        p, rhs = line.split(' => ')
        patterns = set()

        # Generate all rotations and flips
        for _ in range(4):
            patterns.add(p)
            patterns.add(flip(p))
            p = rotate(p)

        # Map all variations to the same enhancement
        for variant in patterns:
            rules[variant] = rhs

    return rules

def split_grid(grid):
    size = len(grid)
    if size % 2 == 0:
        block_size = 2
    else:
        block_size = 3
        
    blocks = []
    for r in range(0, size, block_size):
        for c in range(0, size, block_size):
            block = '/'.join(grid[r+i][c:c+block_size] for i in range(block_size))
            blocks.append(block)

    return blocks, block_size

def join_blocks(blocks, block_size, blocks_per_row):
    new_grid = []

    # Process one row of blocks at a time
    for i in range(0, len(blocks), blocks_per_row):
        # blocks for this row
        row_blocks = blocks[i:i + blocks_per_row]

        # Each block has block_size rows
        for r in range(block_size):
            # Concatenate the r-th row from each block
            new_row = ''.join(block.split('/')[r] for block in row_blocks)
            new_grid.append(new_row)

    return new_grid

def fractal_art(lines, iterations):
    rules = parse_rules(lines)
    grid = [
        ".#.",
        "..#",
        "###"
    ]

    for _ in range(iterations):
        blocks, old_block_size = split_grid(grid)
        enhanced_blocks = [rules[b] for b in blocks]
        new_block_size = len(enhanced_blocks[0].split('/'))
        blocks_per_row = len(grid) // old_block_size
        grid = join_blocks(enhanced_blocks, new_block_size, blocks_per_row)

    return sum(row.count('#') for row in grid)

ans[0] = fractal_art(data, 5)
ans[1] = fractal_art(data, 18)
print(ans)