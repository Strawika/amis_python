a = float(input("Enter a: "))
n = int(input("Enter n: "))


def power(a, n):
    if a <= 0 or n < 0:
        return "Enter correct numbers"
    if n == 0:
        return 1
    else:
        return a*power(a, n-1)


print("a**n= ", power(a, n))
input()
