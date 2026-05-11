from collections import deque

def run_intcode(data, inputs=None):
    """
    Runs the generator VM until it halts.
    
    Returns:
      ascii_output: string of all outputs < 256
      numeric_output: last output >= 256 (if any, else None)
    """
    vm = intcode_vm(data, inputs)
    ascii_output = ""
    numeric_output = None
    
    try:
        output = next(vm)
        while True:
            if output == "INPUT":
                raise RuntimeError("VM requested input, but none provided")
            elif output < 256:
                ascii_output += chr(output)
            else:
                numeric_output = output
            output = next(vm)
    except StopIteration:
        pass
    
    return ascii_output, numeric_output

def get_address(data,i,mode,base):
    if mode == 0:
        return data.get(i, 0)
    elif mode == 1:
        return i
    elif mode == 2:
        return data.get(i,0)+base
    else:
        raise RuntimeError(f"Unsupported parameter mode: {mode}")
        
def get_parameter(data,p):
    if p not in data:
        data[p]=0
    return data[p]

def to_ascii(s):
    return [ord(ch) for ch in s]

def computer(data,inputs,i=0,base=0):
    while True:
        x=data[i]
        i+=1
        opc = x%100
        p1 = x//(10**2)%10
        p1 = get_address(data,i,p1,base)
        if opc==99:
            return data,i,base,None
        if opc in [3,4,9]:
            i+=1
            if opc == 3:
                if not inputs:
                    return data, i, base, 'INPUT'
                data[p1]=inputs.pop(0)
            p1 = get_parameter(data,p1)
            if opc == 4:
                return data,i,base,p1
            elif opc == 9:
                base += p1
        else:
            p2 = x//(10**3)%10
            p2 = get_address(data,i+1,p2,base)
            p1,p2 = get_parameter(data,p1),get_parameter(data,p2)
            if opc in [5,6]:
                if opc == 5:
                    if p1!=0:
                        i = p2-2
                elif opc == 6:
                    if p1==0:
                        i = p2-2
                i+=2
            elif opc in [1,2,7,8]:
                p3 = x//(10**4)%10
                p3 = get_address(data,i+2,p3,base)
                if opc == 1:
                    data[p3]=p1+p2
                elif opc == 2:
                    data[p3]=p1*p2
                elif opc == 7:
                    if p1<p2:
                        data[p3]=1
                    else:
                        data[p3]=0
                elif opc == 8:
                    if p1==p2:
                        data[p3]=1
                    else:
                        data[p3]=0  
                i+=3
                
def intcode_vm(data_init, inputs=None):
    """
    Generator-based Intcode VM.
    
    Yields outputs one by one.
    
    data_init: dict or list of initial memory
    inputs: list, deque, or string (will convert to deque of ASCII codes)
    """
    # Copy memory into a dict
    if isinstance(data_init, list):
        data = {i: v for i, v in enumerate(data_init)}
    else:
        data = dict(data_init)
    
    # Prepare inputs
    if inputs is None:
        inputs = deque()
    elif isinstance(inputs, str):
        inputs = to_ascii(inputs)
    else:
        inputs = deque(inputs)
    
    i = 0
    base = 0
    
    while True:
        instr = data.get(i, 0)
        opcode = instr % 100
        mode1 = (instr // 100) % 10
        mode2 = (instr // 1000) % 10
        mode3 = (instr // 10000) % 10
        
        if opcode == 99:
            return
        
        if opcode in [1,2,7,8]:  # three-parameter instructions
            p1 = get_address(data, i+1, mode1, base)
            p2 = get_address(data, i+2, mode2, base)
            p3 = get_address(data, i+3, mode3, base)
            v1 = get_parameter(data, p1)
            v2 = get_parameter(data, p2)
            
            if opcode == 1:  # add
                data[p3] = v1 + v2
            elif opcode == 2:  # multiply
                data[p3] = v1 * v2
            elif opcode == 7:  # less than
                data[p3] = int(v1 < v2)
            elif opcode == 8:  # equals
                data[p3] = int(v1 == v2)
            
            i += 4
            
        elif opcode in [3,4,9]:  # one-parameter instructions
            p1 = get_address(data, i+1, mode1, base)
            
            if opcode == 3:  # input
                if not inputs:
                    # Wait for input from outside
                    val = yield "INPUT"
                    #if val is None:
                    #    val = -1
                    inputs.append(val)
                
                data[p1] = inputs.popleft()
                i += 2
                
            elif opcode == 4:  # output
                val = get_parameter(data, p1)
                yield val
                i += 2
                
            elif opcode == 9:  # adjust relative base
                base += get_parameter(data, p1)
                i += 2
        
        elif opcode in [5,6]:  # jumps
            p1 = get_address(data, i+1, mode1, base)
            p2 = get_address(data, i+2, mode2, base)
            v1 = get_parameter(data, p1)
            v2 = get_parameter(data, p2)
            
            if opcode == 5:  # jump-if-true
                i = v2 if v1 != 0 else i + 3
            elif opcode == 6:  # jump-if-false
                i = v2 if v1 == 0 else i + 3
        else:
            raise RuntimeError(f"Unknown opcode {opcode} at position {i}")
