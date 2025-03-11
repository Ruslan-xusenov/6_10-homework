def a(numbers):
    numbers_str = list(map(int, numbers.split()))
    operations = []

    for i in range(2, len(numbers_str)):
        a, b, q = numbers_str[i - 2], numbers_str[i - 1], numbers_str[i]

        if a + b == q:
            operations.append("addition")

        elif a - b == q:
            operations.append("subtraction")

        elif a * b == q:
            operations.append("multiplication")

        elif b!=0 and a // b ==q:
            operations.append("division")

    return ", ".join(operations)

print(a("9 4 5 20 25"))
print(a("2 2 4"))
print(a("10 5 2 3 6"))