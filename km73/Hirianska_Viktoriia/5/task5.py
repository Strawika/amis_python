x=[]
y=[]
isError = False
for i in range(8):
    a=int(input("Enter number x: "))
    x.append(a)
    b=int(input("Enter number y: "))
    y.append(b)
if x<1 or x>8 or y<1 or y>8:
    print("Try to enter the correct number")
for i in range(8):
        for j in range(8):
            if i!=j:
                if abs(x[i]-x[j])==abs(y[i]-y[j]) or x[i]==x[j] or y[i]==y[j]:
                    print("YES")
                    isError= True
                    break           
            else:
                print("NO")
input()
