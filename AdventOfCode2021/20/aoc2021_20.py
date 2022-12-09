"Day 20 of AOC2021"
with open("data.txt", "r") as file:
    data = file.read()
    
iea, input_image = data.split('\n\n')
input_image = input_image.split('\n')

n=50
#qui sto aggiungendo n righe/colonne  di '.' per parte
s=''
for i in range(len(input_image[0])):
    s+='.'
to_add = [s for x in range(n)]
input_image=to_add+input_image+to_add
for i in range(len(input_image)):
    x = ''
    for j in range(n):
        x += '.'
    input_image[i] = x+input_image[i]+x


def enhance(image,rule):
    output_image = [['.' for y in range(len(image[0]))] for x in range(len(image))]
    for i in range(len(output_image)):
        for j in range(len(output_image[0])):
            s = ''
            for ii in [-1,0,1]:
                for jj in [-1,0,1]:
                    if 0<=i+ii<len(image) and 0<=j+jj<len(image[0]):
                        x = image[i+ii][j+jj]
                        if x=='.':
                            s+='0'
                        else:
                            s+='1'
                    else:
                        if image[i][j] == '.':
                            s += '0'
                        else:
                            s += '1'
            s = int(s,2)
            output_image[i][j]=rule[s]
    return output_image

def show(image):
    for line in image:
        s = ''
        for x in line:
            s += x
        print(s)
        
def count(image):
    s = 0
    for line in image:
        for x in line:
            if x=='#':
                s += 1
    return s

for i in range(n):
    input_image = enhance(input_image,iea)
print(count(input_image))
    