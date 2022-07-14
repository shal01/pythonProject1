a=input("enter a word")
r=""
for i in a:
    if i not in r:
        r+=i
    else:
        print(i)
        break