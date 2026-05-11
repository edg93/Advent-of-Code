with open("AoC2024_03_data.txt", "r") as file:
    data = file.read()

ans1,ans2 = 0,0
enable=True

for i in range(len(data)):
    if data[i:i+7]=="don't()":
        enable=False
    if data[i:i+4]=="do()":
        enable=True
    if data[i:i+4]=="mul(":
        j= i+4
        a,b='',''
        while data[j].isnumeric():
            a+=data[j]
            j+=1
        if data[j]!=",":
            continue
        j+=1
        while data[j].isnumeric():
            b+=data[j]
            j+=1
        if data[j]!=")":
            continue
        
        ans1+=int(a)*int(b)

        if enable:
            ans2+=int(a)*int(b)
        
print(ans1,ans2)