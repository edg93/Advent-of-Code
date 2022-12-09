f = open("data.txt", "r")
passports = f.read()
passports=passports.split('\n\n')
f.close()

for k in range(len(passports)):
    passports[k]=passports[k].replace('\n',' ')
    passports[k]=passports[k].split(' ')
    keys = []
    values = []
    for entry in passports[k]:
        entry=entry.split(':')
        keys.append(entry[0])
        values.append(entry[1])
    passports[k] = dict(zip(keys,values))
    if len(passports[k])==7:
        if 'cid' in passports[k].keys():
            passports[k]=0
    elif len(passports[k])<7:
        passports[k]=0
     
passports=[x for x in passports if x!=0]

print(len(passports))
counter=len(passports)
for person in passports:
    ok = True
    if int(person["byr"])<1920 or int(person["byr"])>2002:
        ok = False
    if int(person["iyr"])<2010 or int(person["iyr"])>2020:
        ok = False
    if int(person["eyr"])<2020 or int(person["eyr"])>2030:
        ok = False
    if person["ecl"] not in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']:
        ok = False
    if len(person["pid"])!=9 or not person["pid"].isnumeric():
        ok = False
    if person["hgt"][-2:] not in ['cm', 'in'] or not person["hgt"][:-2].isnumeric():
        ok = False
    if person["hgt"][-2:]=='cm' and (int(person["hgt"][:-2])<150 or int(person["hgt"][:-2])>193):
        ok = False
    if person["hgt"][-2:]=='in' and (int(person["hgt"][:-2])<59 or int(person["hgt"][:-2])>76):
        ok = False
        
    if len(person["hcl"])!=7 or person["hcl"][0]!='#':
        ok = False
    for letter in person["hcl"][1:]:
        if letter not in '0123456789abcdef':
            ok = False
    
    if not ok:
        counter=counter-1
    
print(counter)
        