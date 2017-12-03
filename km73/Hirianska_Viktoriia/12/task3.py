list = input("Enter list of numbers: ").split()
a = []


def group(list, iterator):
    if iterator == len(list):
        return max(a)
    secondlist = "".join(list)
    sum_elem = list.count(list[iterator])
    if (sum_elem - iterator)*str(list[iterator]) in secondlist:
        a.append(sum_elem - iterator)
    return group(list, iterator + 1)


print(group(list, 0))
