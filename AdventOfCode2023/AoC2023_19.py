for file in ["AoC2023_19_test.txt","AoC2023_19_data.txt"]:
    with open(file, "r") as f:
        data = f.read()
    
    workflows,parts = data.split('\n\n')
    ans = [0,0]
    workflows = workflows.splitlines()
    parts = parts.splitlines()
    
    wf_dict = {}
    
    for wf in workflows:
        name, body = wf.split('{')
        rules = body[:-1].split(',')
        parsed = []
        for r in rules:
            if ':' in r:
                cond, dest = r.split(':')
                var, op, val = cond[0], cond[1], int(cond[2:])
                parsed.append((var, op, val, dest))
            else:
                parsed.append((None, None, None, r))
        wf_dict[name] = parsed

        
    def rate(x, m, a, s):
        attrs = {'x': x, 'm': m, 'a': a, 's': s}
        wf = 'in'
        while True:
            for var, op, val, dest in wf_dict[wf]:
                if var is None:
                    if dest == 'A':
                        return True
                    if dest == 'R':
                        return False
                    wf = dest
                    break
                if (op == '<' and attrs[var] < val) or (op == '>' and attrs[var] > val):
                    if dest == 'A':
                        return True
                    if dest == 'R':
                        return False
                    wf = dest
                    break
        
    for part in parts:
        x,m,a,s = part[1:-1].split(',')
        x = int(x[2:])
        m = int(m[2:])
        a = int(a[2:])
        s = int(s[2:])
        if rate(x,m,a,s):
            ans[0] += x+m+a+s
                
    def split_range(lo, hi, op, value):
        """
        Split the range [lo, hi] based on condition:
          op is '<' or '>'
          value is the comparison value
        Returns:
          (matching_range or None, remaining_range or None)
        """
        if op == '<':
            if hi < value:
                return (lo, hi), None
            if lo >= value:
                return None, (lo, hi)
            return (lo, value - 1), (value, hi)
    
        if op == '>':
            if lo > value:
                return (lo, hi), None
            if hi <= value:
                return None, (lo, hi)
            return (value + 1, hi), (lo, value)
        
    def count(ranges):
        prod = 1
        for lo, hi in ranges.values():
            prod *= (hi - lo + 1)
        return prod
    
    
    ranges = {'x': (1, 4000),'m': (1, 4000),'a': (1, 4000),'s': (1, 4000)}
    stack = [('in', ranges)]
    accepted = []
    while stack:
        wf,ranges = stack.pop()
        if wf == 'A':
            accepted.append(ranges)
            continue
        elif wf == 'R':
            continue
        for var, op, value, dest in wf_dict[wf]:
            if var is None:
                stack.append((dest, ranges))
                break
            lo,hi = ranges[var]
            matching,rest = split_range(lo,hi,op,value)
            if matching:
                new_ranges = ranges.copy()
                new_ranges[var] = matching
                stack.append((dest,new_ranges))
            if rest:
                ranges[var] = rest
                
    ans[1] = sum(count(r) for r in accepted)
    print(ans)