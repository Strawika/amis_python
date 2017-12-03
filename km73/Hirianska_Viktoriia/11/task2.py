def minimum(list):
    if len(list) == 0:
        return
    if len(list) == 1: 
        return list[0]
    min = minimum(list[1:])
    return (min if min < list[0] else list[0])


list = input("Enter list of numbers: ").split()


print(minimum(list))
