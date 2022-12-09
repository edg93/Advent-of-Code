f = open("data.txt", "r")
data = f.read()
numbers=data.split('\n')

currentNumbers = numbers[:25]
sums = [[] for k in range(len(currentNumbers)-1)]

for k in range(len(sums)):
    sums[k]=[int(n)+int(currentNumbers[k]) for n in currentNumbers[k+1:]]
    
counter=len(currentNumbers)
failNumber=0

while True:
    if not any(int(numbers[counter]) in sublist for sublist in sums):
        failNumber=int(numbers[counter])
        print(failNumber)
        break
    currentNumbers = currentNumbers[1:]+[numbers[counter]]
    counter = counter+1
    sums = sums[1:]+[[int(currentNumbers[-1])]] #traslo le somme
    for k in range(len(sums)):
        sums[k]=sums[k]+[int(currentNumbers[k])+int(currentNumbers[-1])] #aggiungo solo le nuove somme
        
numbers = numbers[:counter] + numbers[counter+1:] #I remove the number that I have found

for k in range(len(numbers)):
    somma = int(numbers[k])
    listN = [int(numbers[k])]
    counter = 1
    while somma < failNumber:
        somma = somma + int(numbers[k+counter])
        listN = listN + [int(numbers[k+counter])]
        counter = counter + 1

    if somma == failNumber:
        print(listN)
        print(max(listN)+min(listN))
        break
    