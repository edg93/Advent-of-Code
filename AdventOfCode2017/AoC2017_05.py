for file in ["AoC2017_05_data.txt"]:
    with open(file, "r") as f:
        data = f.read()
    data = data.splitlines()
    ans = [0,0]
    
            
    def solve(part2=False):
        jumps = list(map(int, data))
        i,counter = 0,0
        while 0<= i < len(jumps):
            current_i = i
            i += jumps[i]
            counter+=1
            if part2:
                if jumps[current_i]<3:
                    jumps[current_i] += 1
                else:
                    jumps[current_i] -= 1
            else:
                jumps[current_i] += 1
        return counter

    ans[0] = solve()
    ans[1] = solve(True)
    print(ans)