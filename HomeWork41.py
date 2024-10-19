#generallist = [0,1,0,12,3]
#generallist = [0]
#generallist = [1,0,13,0,0,0,5]
generallist = [9,0,7,31,0,45,0,45,0,45,0,0,96,0]

print(generallist)
for IndexList in range(len(generallist)):
    generallist.remove(0)
    generallist.append(0)
print(generallist)