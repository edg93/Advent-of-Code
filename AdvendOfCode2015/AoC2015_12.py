import json

with open("AoC2015_12_data.txt") as f:
    data = json.load(f)


ans = [0,0]

def sum_numbers(obj, ignore_red=False):
    if isinstance(obj, int):
        return obj

    elif isinstance(obj, list):
        return sum(sum_numbers(x, ignore_red) for x in obj)

    elif isinstance(obj, dict):
        if ignore_red and "red" in obj.values():
            return 0
        return sum(sum_numbers(v, ignore_red) for v in obj.values())

    else:
        return 0
    
ans[0] = sum_numbers(data)
ans[1] = sum_numbers(data,True)

print(ans)