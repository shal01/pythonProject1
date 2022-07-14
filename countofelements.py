a=input("enter a string")
s="aeiou"
count=""
for i in a:
    if i not in s:
        count+=i
print(count)




