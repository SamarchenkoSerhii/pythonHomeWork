digit5  = int(input("Please enter a 5-digit number: "))
print( digit5 // 10000 + digit5 // 1000 % 10 * 10 + digit5 // 100 % 10 * 100 + digit5 //10 % 10 *1000 + digit5 % 10 *10000)