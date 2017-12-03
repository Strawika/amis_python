def modifiedfunc(list):
    if len(list) == 1:
        return list[0]
    elif (len(list))%2 != 0:
        return
    else:
        half = len(list)//2
        return list[half:] + list[:half]


list = input("Enter list of numbers: ").split()


print(modifiedfunc(list))









