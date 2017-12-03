def reverse(list):
    if len(list) == 1:
        return list
    else:
        return [list[-1]] + reverse(list[:-1])


list = input("Enter list of numbers: ").split()


print(reverse(list))