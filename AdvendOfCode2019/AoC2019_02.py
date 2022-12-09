for j in range(100):
    for k in range(100):
        with open("AoC2019_02_data.txt", "r") as file:
            data = file.read()

        data = [int(x) for x in data.split(',')]
        data[1],data[2]=j,k
        
        for i in range(len(data)):
            x = data[i]
            if i%4==0:
                i1,i2,i3 = data[i+1:i+4]
                if x == 99:
                    break
                elif x == 1:
                    data[i3]=data[i1]+data[i2]
                elif x == 2:
                    data[i3]=data[i1]*data[i2]
        if j==12 and k==2:
            print(data[0])
        if data[0]==19690720:
            print(data[1],data[2])