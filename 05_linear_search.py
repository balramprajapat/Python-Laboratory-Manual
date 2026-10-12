print("Name: Balram Prajapat")
print("Enrollment No: 0863CS241051")

arr = list(map(int, input("Enter elements: ").split()))
key = int(input("Enter element to search: "))

for i in range(len(arr)):
    if arr[i] == key:
        print("Element found at position", i + 1)
        break
else:
    print("Element not found")
