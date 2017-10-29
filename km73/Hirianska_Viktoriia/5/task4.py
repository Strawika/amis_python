a=[]
n=int(input("Enter the number of pins: "))
k=int(input("Enter the number of throws: "))
for i in range (k):
    a.append((str)(i))
for i in range (k):
    li=int(input("Enter starrt place: "))
    ri=int(input("Enter finish place: "))
    for li in range(ri):
        a[li]="."
    for i in range(li):
        a[i]="I"
    for ri in range(n):
        a[ri]="I"
input()
