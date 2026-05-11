reindeers = {'Vix','Rud','Don','Bli','Com','Cup','Das','Dan','Pra'}
speeds = {'Vix':[19,7],'Rud':[3,15],'Don':[19,9],'Bli':[19,9],'Com':[13,7],'Cup':[25,6],'Das':[14,3],'Dan':[3,16],'Pra':[25,6]}
rest_times = {'Vix':124,'Rud':28,'Don':164,'Bli':158,'Com':82,'Cup':145,'Das':38,'Dan':37,'Pra':143}

ans=[0,0]
T = 2503

points={}

for reindeer in reindeers:
    points[reindeer]=0

for t in range(1,T+1):
    positions= {}

    for reindeer in reindeers:
        speed,time_moving = speeds[reindeer]
        cycle_time = time_moving+rest_times[reindeer]
        n_cycles = t//cycle_time
        rest = t%cycle_time
        
        distance = n_cycles*speed*time_moving+speed*min(rest,time_moving)
        positions[reindeer]=distance
    max_points = max(positions.values())
    leaders = [(k, v)[0] for k, v in positions.items() if v == max_points]
    for leader in leaders:
        points[leader]+=1
    
ans[0]=positions[leaders[0]]
ans[1]=max(points.values())

print(ans)