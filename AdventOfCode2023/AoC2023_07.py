with open("AoC2023_07_data.txt", "r") as file:
    data = file.read()
    
data = data.split('\n')

hands = {}

for p in [1,2]:
    hand_types = {'5':[],'14':[],'23':[],'113':[],'122':[],'1112':[],'11111':[]}
    code = {'K':'B','Q':'C','J':'D','T':'E','9':'F','8':'G','7':'H','6':'I','5':'J','4':'K','3':'L','2':'M'}
    f_partition = {'':'5','1':'5','11':'14','111':'113','1111':'1112','12':'14','112':'113','13':'14','22':'23','4':'5','3':'5','2':'5'}
    
    for hand in data:
        cards,bid = hand.split()
        for x,y in code.items():    
            cards = cards.replace(x,y)
        if p==2:
            cards = cards.replace(code['J'],'Z')
        hands[cards] = int(bid)
        n = {1:0,2:0,3:0,4:0,5:0}
        letters_done = set()
        for letter in cards:
            #in part 2 I dont count the jokers in the hand
            if p==2:
                letters_done.add('Z')
            if letter not in letters_done:
                n[cards.count(letter)]+=1
                letters_done.add(letter)
        partition = ''
        for a,c in n.items():
            for _ in range(c):
                partition += str(a)
        if p == 2 and 'Z' in cards :
            #in part 2, if I have jokers in the hand, I first transform the partition "transforming" "the jokers into the best cards
            partition = f_partition[partition]
        hand_types[partition].append(cards)
    ans=0
    c = len(data)
    for _,hand_list in hand_types.items():
        hand_list.sort()
        for hand in hand_list:
            ans += c*hands[hand]
            c-=1
    print(ans)