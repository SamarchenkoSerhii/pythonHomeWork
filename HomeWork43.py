import random
generallist = []
for IndexList in range(random.randint(3,10)):
    generallist.append(random.randint(1,9))
NewList = generallist[0] , generallist[2] , generallist[IndexList-1]
print(generallist )
print(NewList )