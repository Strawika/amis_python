a = float(input("Enter a: "))
n = int(input("Enter n: "))


def power(a, n):
    if a <= 0:
        return "Enter correct number"
    if n == 0:
        return 1
    elif n > 0:
        return a * power(a, n - 1)
    else:
        return (1 / a) * power(a, n + 1)


print(power(a, n))
input()
