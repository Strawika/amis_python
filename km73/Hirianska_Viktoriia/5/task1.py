a=[]
c=int(input("Enter the number of classmates: "))
p=int(input("Enter the height of Peter: "))
if p<100 or p>200:
    print("You entered the wrong height")
j=1
for i in range(c):
    e=int(input("Enter the height of classmate: "))
    if e<100 or e>200:
        print("You entered the wrong height")
    a.append(e)
    if a[i]>=p:
        j+=1
print("Peter is",j)
input()


