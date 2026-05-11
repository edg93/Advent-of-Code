from hashlib import md5

ans = [0,0]

door_id = "ugkcyxxp"  # replace with your input

password = ""

password_2 = [None for _ in range(8)]
i = 0

while len(password) < 8 or None in password_2:
    h = md5((door_id + str(i)).encode()).hexdigest()
    if h.startswith("00000"):
        index = h[5]
        if index in '01234567' and password_2[int(index)] is None:
            password_2[int(index)]=h[6]
        if len(password)<8:
            password += h[5]
    i += 1

ans[0] = password
ans[1] = ''.join(password_2)
print(ans)