with open("AoC2023_09_data.txt", "r") as file:
    data = file.read()

data = data.split('\n')    

def all_zeros(L):
    for x in L:
        if x!=0:
            return False
    return True

ans1,ans2=0,0
for line in data:
    right,left = [],[]
    L = [int(x) for x in line.split()]
    while not all_zeros(L):
        right.append(L[-1])
        left.append(L[0]*(-1)**(len(left)%2))
        L = [L[i+1] - L[i] for i in range(len(L)-1)]
    ans1+=sum(right)
    ans2+=sum(left)

print(ans1,ans2)