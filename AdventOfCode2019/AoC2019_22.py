with open("AoC2019_22_data.txt") as f:
    data = f.read().splitlines()

ans = [0,0]

i = 2019
deck_size = 10007



def find_ab(data,deck_size):
    a,b = 1,0

    for line in data:
        line = line.split()
        if line[0] == 'cut':
            new_a,new_b = 1,-int(line[-1])
        elif line[1] == 'with':
            new_a,new_b = int(line[-1]),0
        else:
            new_a,new_b = -1,-1
        a,b = (a*new_a) % deck_size, (b*new_a+new_b) % deck_size
          
    return a,b

a,b = find_ab(data,deck_size)
ans[0] = (a*i+b) % deck_size

deck_size = 119315717514047
a,b = find_ab(data,deck_size)

    
k = 101741582076661
A_k = pow(a,k,deck_size)
if a == 1:
    B_k = (b * k) % deck_size
else:
    B_k = b * (1 - A_k) * pow(1-a,-1,deck_size) % deck_size

ans[1] = ((2020-B_k) * pow(A_k,-1,deck_size))%deck_size
print(ans)