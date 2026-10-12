print("Name: Balram Prajapat")
print("Enrollment No: 0863CS241051")

arr = list(map(int, input("Enter sorted elements: ").split()))
key = int(input("Enter element to search: "))

low, high = 0, len(arr) - 1

while low <= high:
    mid = (low + high) // 2

    if arr[mid] == key:
        print("Element found at position", mid + 1)
        break
    elif arr[mid] < key:
        low = mid + 1
    else:
        high = mid - 1
else:
    print("Element not found")
