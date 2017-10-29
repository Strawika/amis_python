a=[]
k=int(input("Enter number of elements: ")) 
for i in range(k):
    b=input("Enter element: ")
    a.append(b)
c=[]
for b in a:
    if a.count(b)==1:
        c.append(b)
print("Non-repeated numbers: ",c)
input()
