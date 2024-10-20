generallist = [0, 1, 7, 2, 4, 8]
#generallist =[1, 3, 5]
#generallist =[6]
#generallist =[]

summ = 0
for IndexList in range(len(generallist)):
    if IndexList%2 == 0 :
        summ = summ+generallist[IndexList]
if len(generallist) != 0 :
    summ = summ * generallist[len(generallist)-1]
print(generallist,"=>",summ)



