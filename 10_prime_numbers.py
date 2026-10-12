print("Name: Balram Prajapat")
print("Enrollment No: 0863CS241051")

n = int(input("Enter N: "))
count = 0
num = 2

while count < n:
    prime = True

    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            prime = False
            break

    if prime:
        print(num, end=" ")
        count += 1

    num += 1

print()
