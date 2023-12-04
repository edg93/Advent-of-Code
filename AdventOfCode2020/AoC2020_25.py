data = (5099500,7648211)


def transform(x, sz):
    return pow(x, sz, 20201227)

l1 = 0
while transform(7, l1) != data[0]:
    l1 += 1

l2 = 0
while transform(7, l2) != data[1]:
    l2 += 1

encryption = transform(data[0], l2)
print(encryption)