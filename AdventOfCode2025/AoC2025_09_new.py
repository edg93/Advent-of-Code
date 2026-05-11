from collections import defaultdict
from itertools import combinations

# ------------------------------------------------------------
# Parse input
# ------------------------------------------------------------

def parse_points(text):
    points = []
    for line in text.strip().splitlines():
        x, y = map(int, line.split(","))
        points.append((x, y))
    return points


# ------------------------------------------------------------
# Build polygon edges (closed loop)
# ------------------------------------------------------------

def polygon_edges(points):
    edges = []
    n = len(points)
    for i in range(n):
        x1, y1 = points[i]
        x2, y2 = points[(i + 1) % n]
        edges.append((x1, y1, x2, y2))
    return edges


# ------------------------------------------------------------
# Scanline fill: build interior intervals per row
# ------------------------------------------------------------

def build_row_intervals(edges):
    events = defaultdict(list)

    for x1, y1, x2, y2 in edges:
        if x1 == x2:  # vertical edge
            if y1 < y2:
                y_start, y_end = y1, y2
            else:
                y_start, y_end = y2, y1

            # half-open rule [y_start, y_end)
            for y in range(y_start, y_end):
                events[y].append(x1)
    row_intervals = {}
    for y, xs in events.items():
        xs.sort()
        intervals = set()
        for i in range(0, len(xs), 2):
            intervals.add((xs[i], xs[i + 1]))
        row_intervals[y] = intervals

    for x1, y1, x2, y2 in edges:
        if y1==y2:
            if y1 in row_intervals.keys():
                row_intervals[y1].add((min(x1,x2),max(x1,x2)))
            else:
                row_intervals[y1] = {(min(x1,x2),max(x1,x2))}
    return row_intervals


# ------------------------------------------------------------
# Check if a row fully covers [x1, x2]
# ------------------------------------------------------------

def row_covers(row_intervals, y, x1, x2):
    for a, b in row_intervals.get(y, []):
        if a <= x1 and x2 <= b:
            return True
    return False


# ------------------------------------------------------------
# Solve Part 2
# ------------------------------------------------------------

def solve_part2(points):

    max_area = 0

    for (x1, y1), (x2, y2) in combinations(points, 2):
        print(x1,x2)
        x_lo, x_hi = sorted((x1, x2))
        y_lo, y_hi = sorted((y1, y2))
        area = (x_hi - x_lo+1) * (y_hi - y_lo+1)
        if  area <= max_area:
            continue
        
        valid = True
        for y in range(y_lo, y_hi+1):
            
            if not row_covers(row_intervals, y, x_lo, x_hi):
                valid = False
                break
        
        if valid:
            max_area = area

    return max_area


# ------------------------------------------------------------
# Main
# ------------------------------------------------------------

with open("AoC2025_09_data.txt") as f:
    data = f.read()
points = parse_points(data)
edges = polygon_edges(points)
row_intervals = build_row_intervals(edges)
answer = solve_part2(points)
print(answer)
