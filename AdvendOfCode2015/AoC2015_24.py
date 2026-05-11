from itertools import combinations
from math import prod
from functools import lru_cache

gifts = [1,2,3,7,11,13,17,19,23,31,37,41,43,47,53,59,61,67,71,73,79,83,89,97,101,103,107,109,113]
ans = [0,0]

@lru_cache(maxsize=None)
def can_split(packages, g, target):
    if g == 1:
        return sum(packages) == target
    n = len(packages)
    for size in range(1, n + 1):
        for combo in combinations(packages, size):
            if sum(combo) == target:
                remaining = tuple(x for x in packages if x not in combo)
                if can_split(remaining, g - 1, target):
                    return True
    return False

def find_ideal_first_group_fast(packages, groups=4):
    total_weight = sum(packages)
    target_weight = total_weight // groups

    packages = tuple(sorted(packages, reverse=True))
    best_qe = None

    for size in range(1, len(packages)):
        for combo in combinations(packages, size):
            if sum(combo) == target_weight:
                remaining = tuple(x for x in packages if x not in combo)
                if can_split(remaining, groups - 1, target_weight):
                    qe = prod(combo)
                    if best_qe is None or qe < best_qe:
                        best_qe = qe
        if best_qe:  # minimal size found
            break

    return best_qe

# Example usage
ans[0] = find_ideal_first_group_fast(gifts, groups=3)
ans[1] = find_ideal_first_group_fast(gifts, groups=4)
print(ans)