print("Name: Balram Prajapat")
print("Enrollment No: 0863CS241051")

numbers = list(map(int, input("Enter numbers: ").split()))
maximum = numbers[0]

for num in numbers:
    if num > maximum:
        maximum = num

print("Maximum =", maximum)
