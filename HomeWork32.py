#messageinline = [12,3,4,10]
#messageinline = [1]
#messageinline = []
#messageinline = [12,3,4,10,8]
messageinline = ["fun","code","is"]
print(messageinline[0:])
if len(messageinline)>1 :
    messageinline = (messageinline[len(messageinline)-1:])+(messageinline[0:len(messageinline)-1])
print(messageinline)
