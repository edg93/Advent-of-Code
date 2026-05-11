from time import time


t1= time()
for file in ["AoC2025_03_test.txt","AoC2025_03_data.txt"]:
    with open(file, "r") as file:
        data = file.read()
        
    ans = [0,0]
    
    parts = [2,12]
 
    for line in data.split('\n'):
        for n in parts:
            index=-1
            joltage = ''
            while n>0:
                if n==1:
                    joltage += max(line[index+1:])
                else:
                    joltage += max(line[index+1:-(n-1)])
                for i,battery in enumerate(line):
                    if battery == joltage[-1] and i>index:
                        index = i
                        break
                n-=1
            if len(joltage)==2:
                ans[0]+=int(joltage)
            else:
                ans[1]+=int(joltage)
        
    print(ans)
