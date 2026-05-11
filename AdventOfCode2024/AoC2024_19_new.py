from functools import lru_cache
from collections import defaultdict

for file in ["AoC2024_19_test.txt", "AoC2024_19_data.txt"]:
    with open(file, "r") as f:
        data = f.read().strip()

    patterns, designs = data.split("\n\n")
    patterns = patterns.split(", ")
    designs = designs.splitlines()

    # Optional optimization: group patterns by first character
    patterns_by_first = defaultdict(list)
    for p in patterns:
        patterns_by_first[p[0]].append(p)

    @lru_cache(None)
    def ways(s):
        """Return number of ways to build string s."""
        if s == "":
            return 1

        total = 0
        for p in patterns_by_first.get(s[0], []):
            if s.startswith(p):
                total += ways(s[len(p):])
        return total

    ans = [0,0]

    for d in designs:
        w = ways(d)
        if w > 0:
            ans[0] += 1
        ans[1] += w

    print(ans)