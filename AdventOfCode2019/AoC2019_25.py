from IntcodeComputer import intcode_vm
from itertools import combinations


def send_command(vm, command):
    """Send a text command to the Intcode VM and collect the ASCII output."""
    for ch in command + '\n':
        output = vm.send(ord(ch))
    # Collect all outputs until next INPUT
    result = []
    while True:
        try:
            if output == "INPUT":
                break
            result.append(chr(output))
            output = next(vm)
        except StopIteration:
            break
    return ''.join(result)


with open("AoC2019_25_data.txt", "r") as file:
    data = file.read()
    
data = [int(x) for x in data.split(',')]

vm = intcode_vm(data)
output = next(vm)  # Start generator

send_command(vm,'')
send_command(vm,'south')
send_command(vm,'west')
send_command(vm,'take hologram')
send_command(vm,'south')
send_command(vm,'west')
send_command(vm,'west')
send_command(vm,'take hypercube')
send_command(vm,'east')
send_command(vm,'east')
send_command(vm,'north')
send_command(vm,'east')
send_command(vm,'south')
send_command(vm,'west')
send_command(vm,'north')
send_command(vm,'take coin')
send_command(vm,'south')
send_command(vm,'east')
send_command(vm,'take cake')
send_command(vm,'east')
send_command(vm,'south')
send_command(vm,'east')
send_command(vm,'south')
print(send_command(vm,'south'))


items = ['hologram', 'food ration', 'space law space brochure', 'cake', 'astrolabe', 'wreath', 'coin', 'hypercube']
def try_combinations(items):
    for n in range(1, len(items)+1):
        for combo in combinations(items, n):
            # Drop everything first
            for item in items:
                send_command(vm, f"drop {item}")
            # Take items in combo
            for item in combo:
                send_command(vm, f"take {item}")
            # Try to go through the checkpoint
            output = send_command(vm, "south")  # or the direction of checkpoint
            if "You may proceed" in output:
                print("Success combo:", combo)
                print(output)
                break