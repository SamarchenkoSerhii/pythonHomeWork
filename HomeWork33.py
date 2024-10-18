#generallist = [1,2,3,4,5,6]
#generallist = [1,2,3]
generallist = [1,2,3,4,5]
#generallist = [1]
#generallist = []
print(generallist)
listoflists = [[],[]]
if len(generallist)>1 :
    listoflists[1] = generallist[len(generallist)-len(generallist)-len(generallist)//2:]
    listoflists[0] = generallist[ : len(generallist)-len(generallist)//2]
elif len(generallist)==1:
    listoflists[0] = generallist
print(listoflists)