import string
StringToHashteG = str(input("Enter a string : "))
HashtaG = "# "
HashtagFin = ""
for IndexString in range(len(StringToHashteG)):
    skip = True
    for IndexPunktuation in  range(len(string.punctuation)):
        if StringToHashteG[IndexString] == string.punctuation[IndexPunktuation]  :
            skip = False
    if skip : HashtaG = HashtaG + StringToHashteG[IndexString]
HashtaG = HashtaG.title()

for IndexString in range(len(HashtaG)):
    if IndexString <= 140 and HashtaG[IndexString] != " ":
        HashtagFin = HashtagFin+HashtaG[IndexString]

print(HashtagFin)
