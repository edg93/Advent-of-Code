import numpy as np
import matplotlib.pyplot as plt
from matplotlib import colors

# -----------------------------
# Constants and color mapping
# -----------------------------
EMPTY = ' '
CLAY = '#'
WATER = '|'
STILL = '~'
SPRING = '+'

COLOR_MAP = {
    EMPTY: 0,
    CLAY:  1,
    WATER: 2,
    STILL: 3,
    SPRING: 4,
}

cmap = colors.ListedColormap([
    "white",   # EMPTY
    "black",   # CLAY
    "blue",    # flowing |
    "cyan",    # still ~
    "red",     # spring +
])

plt.ion()  # enable interactive mode

# -----------------------------
# Parsing input
# -----------------------------
def parsing(filename):
    with open(filename, "r") as file:
        data = file.read().strip().split('\n')

    clay = set()
    xmin, xmax = 10**9, 0
    ymin, ymax = 10**9, 0

    for line in data:
        a, b = line.split(', ')
        if a[0] == 'x':
            x = int(a[2:])
            y0, y1 = map(int, b[2:].split('..'))
            for y in range(y0, y1 + 1):
                clay.add((x, y))
            xmin = min(xmin, x)
            xmax = max(xmax, x)
            ymin = min(ymin, y0)
            ymax = max(ymax, y1)
        else:
            y = int(a[2:])
            x0, x1 = map(int, b[2:].split('..'))
            for x in range(x0, x1 + 1):
                clay.add((x, y))
            xmin = min(xmin, x0)
            xmax = max(xmax, x1)
            ymin = min(ymin, y)
            ymax = max(ymax, y)

    # expand boundaries for water spread
    xmin -= 1
    xmax += 1

    return clay, xmin, xmax, ymin, ymax

# -----------------------------
# Grid helpers
# -----------------------------
def tx(x):
    """Translate x coordinate to grid index"""
    return x - xmin

def create_grid(h, w, clay):
    """Create the initial grid with clay and spring"""
    G = [[EMPTY for _ in range(w)] for _ in range(h)]
    for x, y in clay:
        G[y][tx(x)] = CLAY
    G[0][tx(500)] = SPRING
    return G

def grid_to_array_crop(G, ymin, ymax):
    """Convert a portion of the grid to a numeric array for plotting"""
    h = ymax - ymin
    w = len(G[0])
    A = np.zeros((h, w), dtype=int)
    for y in range(ymin, ymax):
        for x in range(w):
            A[y - ymin, x] = COLOR_MAP[G[y][x]]
    return A

# -----------------------------
# STEP 1: Vertical water flow with live plot
# -----------------------------
def flow_live(x, y, G, ymax_grid):
    while True:
        if y > ymax_grid:
            return None

        gx = tx(x)

        # mark flowing water
        if G[y][gx] == EMPTY:
            G[y][gx] = WATER

       
        # check below
        if y + 1 > ymax_grid:
            return None

        below = G[y + 1][gx]

        if below == EMPTY or below == WATER:
            y += 1
            continue

        return (x, y)

def spread_flow(x, y, G):
    """
    Spread water left and right from bottom (x, y)
    1) Mark flowing water '|'
    2) Track leak points for new vertical flow
    3) Convert to still water '~' only after fully contained
    """
    leak_points = []

    # -------------------------
    # Scan left
    # -------------------------
    left = x
    while True:
        gx = tx(left)
        if G[y][gx] == CLAY:
            left += 1  # step back into last empty
            break
        below = G[y+1][gx]
        if below in [EMPTY, WATER]:
            # water leaks downward → start new vertical flow
            leak_points.append((left, y))
            break
        # mark flowing water if empty
        if G[y][gx] == EMPTY:
            G[y][gx] = WATER
            # update plot live
        left -= 1

    # -------------------------
    # Scan right
    # -------------------------
    right = x
    while True:
        gx = tx(right)
        if G[y][gx] == CLAY:
            right -= 1
            break
        below = G[y+1][gx]
        if below in [EMPTY, WATER]:
            leak_points.append((right, y))
            break
        if G[y][gx] == EMPTY:
            G[y][gx] = WATER
            # update plot live
            
        right += 1

    # -------------------------
    # Determine containment
    # -------------------------
    # Check left blocked
    left_blocked = (
        xmin <= left-1 <= xmax and
        G[y][tx(left-1)] == CLAY
    )
    
    # Check right blocked
    right_blocked = (
        xmin <= right+1 <= xmax and
        G[y][tx(right+1)] == CLAY
    )

    if left_blocked and right_blocked:
        # Convert flowing water to still water
        for xx in range(left, right+1):
            gx = tx(xx)
            if G[y][gx] == WATER:
                G[y][gx] = STILL
        leak_points.append((x,y-1))

    return leak_points

# -----------------------------
# Count water function (for Part 1)
# -----------------------------
def count_water(G, ymin_grid, ymax_grid,flowing_water=True):
    """
    Count the number of tiles with water (flowing '|' or still '~')
    in the vertical range ymin_grid..ymax_grid
    """
    counter = 0
    for y in range(ymin_grid, ymax_grid+1):
        counter += sum(1 for cell in G[y] if cell == STILL)
        if flowing_water:
            counter += sum(1 for cell in G[y] if cell == WATER)
    return counter

def simulate(G, start_x=500, im=None, fig=None):
    stack = [(start_x, 0)]  # points to process

    while stack:
        x, y = stack.pop()
        bottom = flow_live(x, y, G, ymax_grid=ymax)
        if im is not None and fig is not None:
            crop_start = max(0, y - 200 // 2)
            crop_end = crop_start + 200
            A = grid_to_array_crop(G, ymin=crop_start, ymax=crop_end)
            im.set_data(A)
            fig.canvas.draw_idle()
            fig.canvas.flush_events()
            plt.pause(pause)
        if bottom is None:
            continue
        # horizontal spread
        leaks = spread_flow(bottom[0], bottom[1], G)
        stack.extend(leaks)
        if im is not None and fig is not None:
            crop_start = max(0, y - 200 // 2)
            crop_end = crop_start + 200
            A = grid_to_array_crop(G, ymin=crop_start, ymax=crop_end)
            im.set_data(A)
            fig.canvas.draw_idle()
            fig.canvas.flush_events()
            plt.pause(pause)
# -----------------------------
# Initialization
# -----------------------------
# Example contest settings:
clay, xmin, xmax, ymin, ymax = parsing("AoC2018_17_data.txt")

WIDTH = xmax - xmin + 1
HEIGHT = ymax + 1

G = create_grid(HEIGHT, WIDTH, clay)

# Create figure and initial image
im,fig = None,None
fig, ax = plt.subplots(figsize=(15, 20))  # taller figure
im = ax.imshow(grid_to_array_crop(G, ymin=0, ymax=200),cmap=cmap, origin='upper', aspect='auto')  # let matplotlib stretch
ax.axis('off')

# force initial draw
if im is not None:
    fig.canvas.draw()
    fig.canvas.flush_events()
pause = 0.001

simulate(G, start_x=500,im=im,fig=fig)

total_water = count_water(G, ymin, ymax,flowing_water = True)
print(f"Total water tiles (part 1): {total_water}")
total_water = count_water(G, ymin, ymax,flowing_water = False)
print(f"Total water tiles (part 2): {total_water}")