print("Name: Balram Prajapat")
print("Enrollment No: 0863CS241051")

n = float(input("Enter a positive number: "))

if n < 0:
    print("Square root not possible")
elif n == 0:
    print("Square root =", 0)
else:
    x = n
    for i in range(10):
        x = (x + n / x) / 2
    print("Square root =", x)
