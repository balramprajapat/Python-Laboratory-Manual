print("Name: Balram Prajapat")
print("Enrollment No: 0863CS241051")

base = int(input("Enter base: "))
power = int(input("Enter power: "))

result = 1
for i in range(power):
    result *= base

print("Result =", result)
