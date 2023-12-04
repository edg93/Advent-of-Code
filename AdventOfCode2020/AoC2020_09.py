with open("AoC2020_09_data.txt", "r") as file:
    data = file.read()
numbers=data.split('\n')

currentNumbers = numbers[:25]
sums = [[int(n)+int(currentNumbers[k]) for n in currentNumbers[k+1:]] for k in range(len(currentNumbers)-1)]
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
        somma += int(numbers[k+counter])
        listN.append(int(numbers[k+counter]))
        counter += 1

    if somma == failNumber:
        print(max(listN)+min(listN))
        break