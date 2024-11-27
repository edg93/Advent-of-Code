with open("AoC2023_04_data.txt", "r") as file:
    data = file.read()
    
data = data.split('\n')
ans1,ans2 = 0,0
copies = [1 for line in data]

for line in data:
    n,rest = line.split(':')
    n = int(n.split()[-1])
    winning_n,your_n = rest.split(' | ')
    winning_n = [int(x) for x in winning_n.split()]
    your_n = [int(x) for x in your_n.split()]
    count = len(set(winning_n) & set(your_n))
    ans1+=int(2**(count-1))
    for i in range(count):
        copies[n+i]+=copies[n-1]
    
ans2=sum(copies)
print(ans1,ans2)