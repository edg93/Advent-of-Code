data = [43,3,4,10,21,44,4,6,47,41,34,17,17,44,36,31,46,9,27,38]
ans = [0,0]
total = 150

def count_combinations(containers, target):
    containers = sorted(containers)  # sorting is optional but helps pruning

    def dfs(index, remaining):
        # Found a valid combination
        if remaining == 0:
            return 1
        # Ran out of containers or exceeded volume
        if remaining < 0 or index == len(containers):
            return 0

        # Choice 1: use this container
        use_it = dfs(index + 1, remaining - containers[index])

        # Choice 2: skip this container
        skip_it = dfs(index + 1, remaining)

        return use_it + skip_it

    return dfs(0, target)

def min_container_combinations(containers, target):
    containers = sorted(containers)
    min_used = float('inf')
    ways = 0

    def dfs(index, remaining, used):
        nonlocal min_used, ways

        if remaining == 0:
            if used < min_used:
                min_used = used
                ways = 1
            elif used == min_used:
                ways += 1
            return
        
        if remaining < 0 or index == len(containers) or used > min_used:
            return
        
        dfs(index + 1, remaining - containers[index], used + 1)
        dfs(index + 1, remaining, used)

    dfs(0, target, 0)
    return min_used, ways


ans[0] = count_combinations(data,total)
ans[1] = min_container_combinations(data,total)[1]
print(ans)