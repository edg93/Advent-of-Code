from collections import deque
data = 3017957

elves = deque(range(1, data+1))

ans = [0,0]
    
while len(elves) > 1:
    elves.append(elves.popleft())  # move current elf to the end
    elves.popleft()                 # remove next elf

ans[0] = elves[0]

left = deque(range(1, data//2 + 1))
right = deque(range(data//2 + 1, data + 1))

while left and right:
    # Remove the elf across (front of right)
    right.popleft()
    
    # Move current elf to the end of right
    right.append(left.popleft())
    
    # Balance the queues
    if len(left) < len(right)-1:
        left.append(right.popleft())

# The last elf is in whichever queue is non-empty

ans [1] = left[0] if left else right[0]
print(ans)