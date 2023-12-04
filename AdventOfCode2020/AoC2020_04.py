with open("AoC2020_04_data.txt", "r") as file:
    data = file.read()
passports=data.split('\n\n')

ans1, ans2 = 0,0
for passport in passports:
    passport = passport.replace('\n',' ').split(' ')
    d = {}
    for entry in passport:
        entry=entry.split(':')
        d[entry[0]]=entry[1]
    if len(passport)==7 and 'cid' in d.keys():
        continue
    if len(passport)<7:
        continue
    ans1+=1
    if not 1920<=int(d["byr"])<=2002:
        continue
    if not 2010<=int(d["iyr"])<=2020:
        continue
    if not 2020<=int(d["eyr"])<=2030:
        continue
    if d["ecl"] not in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']:
        continue
    if len(d["pid"])!=9 or not d["pid"].isnumeric():
        continue
    if d["hgt"][-2:] not in ['cm', 'in'] or not d["hgt"][:-2].isnumeric():
        continue
    if d["hgt"][-2:]=='cm' and not 150<=int(d["hgt"][:-2])<=193:
        continue
    if d["hgt"][-2:]=='in' and not 59<=int(d["hgt"][:-2])<=76:
        continue
    if len(d["hcl"])!=7 or d["hcl"][0]!='#':
        continue
    for letter in d["hcl"][1:]:
        if letter not in '0123456789abcdef':
            continue
    ans2 += 1
    
print(ans1)
print(ans2)
        