print("Name: Balram Prajapat")
print("Enrollment No: 0863CS241051")

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

while b != 0:
    a, b = b, a % b

print("GCD =", a)
