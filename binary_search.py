def binary_search(arr, key):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == key:
            print("Successful")
            return
        elif arr[mid] < key:
            left = mid + 1
        else:
            right = mid - 1
    print("Failed")

print("Name: Priti Paudel Jaisi, Roll_no: 10")
arr = list(map(int, input("Enter the elements (comma-separated): ").split(',')))
arr.sort()  # Binary search requires a sorted array
key = int(input("Enter the element to search for: "))

binary_search(arr, key)
