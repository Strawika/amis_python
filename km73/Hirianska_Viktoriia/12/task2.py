list = input("Enter list of numbers: ").split()
i = len(list)-1
counter = 0


def maxcounter(list,i):
    global counter
    if list[i] == max(list):
        counter += 1
    if i==0:
        return counter
    else:
        return maxcounter(list, i-1)
    
    
print(maxcounter(list,i))


input()
