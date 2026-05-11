with open("AoC2015_02_data.txt", "r") as file:
     data = file.read()
     
     data = data.split('\n')
     ans = [0,0]
     
     for line in data:
         w,l,h = map(int,line.split('x'))
         areas = [w*l,l*h,w*h]
         p = min([w+l,h+l,h+w])
         ans[0] += min(areas)+2*sum(areas)
         ans[1] += 2*p+w*h*l
     
     print(ans)