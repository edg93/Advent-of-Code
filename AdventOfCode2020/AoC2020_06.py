with open("AoC2020_06_data.txt", "r") as file:
    data = file.read()

data=data.split('\n\n')

ans1,ans2 = 0,0

for group in data:
    questions = set()
    group = group.split('\n')
    for person in group:
        for question in person:
            questions.add(question)
    ans1 += len(questions)
    for question in questions:
        ok = True
        for person in group:
            if question not in person:
                ok = False
                break
        if ok:
            ans2 += 1
    
print(ans1)
print(ans2)