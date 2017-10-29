a=[]
n=int(input("Enter the number of elements: ")) 
for i in range(n):
    b=input("Enter the element: ")
    a.append(b)
l=0
for i in range(len(a)-1):
    for j in range(i+1, len(a)):
        if a[i]==a[j]:
            l+=1
print("Number of pairs ",l)
input()
