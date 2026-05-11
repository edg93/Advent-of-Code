from time import time

t1= time()
for file in ["AoC2025_02_test.txt","AoC2025_02_data.txt"]:
    with open(file, "r") as file:
        data = file.read()
        
    ans1,ans2 = 0,0
        
    invalid_ID_1,invalid_ID_2 = set(),set()
    
    
    for line in data.split(','):
        a,b = line.split('-')
        l = len(a)
        for n in range(2,len(b)+1):
            if l%n==0:
                 sequence = a[:l//n]
            else:
                sequence =str(10**(l//n))
            while int(sequence*n)<int(a):
                sequence = str(int(sequence)+1)
            while True:
                ID = sequence*n
                if int(ID)<=int(b) and int(ID)>=int(a):
                    invalid_ID_2.add(ID)
                    if n==2:
                        invalid_ID_1.add(ID)
                    sequence = str(int(sequence)+1)
                else:
                    break
        
    for ID in invalid_ID_1:
        ans1+=int(ID)
    
    for ID in invalid_ID_2:
        ans2+=int(ID)
    
    print(ans1,ans2)
print(time()-t1)
