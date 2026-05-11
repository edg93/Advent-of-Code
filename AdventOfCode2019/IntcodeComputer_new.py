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

def get_address(data, i, mode, base):
    """Compute the address for writes or reads based on parameter mode."""
    if mode == 0:   # position
        return data[i]
    elif mode == 1: # immediate
        return i
    elif mode == 2: # relative
        return data[i] + base
    else:
        raise RuntimeError(f"Unsupported parameter mode: {mode}")

def get_parameter(data, p):
    """Return the value at address p, defaulting to 0."""
    if p not in data:
        data[p] = 0
    return data[p]

def to_ascii(s):
    """Convert string to ASCII code list for Intcode input."""
    return deque(ord(c) for c in s)

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
                    data[p1] = val
                else:
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
