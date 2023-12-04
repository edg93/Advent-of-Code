with open("AoC2019_08_data.txt", "r") as file:
    data = file.read()

data = [int(x) for x in data]

DIM = (25,6)
area = DIM[0]*DIM[1]
layers = []

def show(image):
    for i in range(DIM[1]):
        print(image[i*DIM[0]:(i+1)*DIM[0]])

for i in range(len(data)//area):
    layers.append(data[i*area:(i+1)*area])
    
d = []
for i,layer in enumerate(layers):
    zeros = layer.count(0)
    d.append((layer.count(0),layer.count(1),layer.count(2)))

print(min(d)[1]*min(d)[2])

image = ''
for i in range(len(layers[0])):
    for layer in layers:
        if layer[i]!=2:
            if layer[i]==1:
                image += '#'
            else:
                image += ' '
            break
show(image)