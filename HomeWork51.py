import keyword
import string

StringForVariable = input("Enter a String: ")
ResultOfTheCheck = True

for IndexVariable in range(len(string.punctuation)):
    if StringForVariable.find(string.punctuation[IndexVariable]) != -1 :
        ResultOfTheCheck = False
        if string.punctuation[IndexVariable] == "_" :
            ResultOfTheCheck = True

if StringForVariable[0].isdigit():
    ResultOfTheCheck = False

if not StringForVariable.islower():
    ResultOfTheCheck = False

for IndexVariable in range(len(StringForVariable)-1):
    if StringForVariable[IndexVariable] == "_" and  StringForVariable[IndexVariable+1] == "_" :
        ResultOfTheCheck = False

for IndexVariable in range(len(StringForVariable)):
    if StringForVariable[IndexVariable] == " " :
        ResultOfTheCheck = False

for IndexVariable in range(len(keyword.kwlist)):
    if (keyword.kwlist[IndexVariable]) == StringForVariable :
        ResultOfTheCheck = False


print(ResultOfTheCheck)