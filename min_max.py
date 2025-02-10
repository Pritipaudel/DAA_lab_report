def find_min_max(arr):
    min_val = arr[0]
    max_val = arr[0]
    for num in arr:
        if num < min_val:
            min_val = num
        if num > max_val:
            max_val = num
    print("Minimum value:", min_val)
    print("Maximum value:", max_val)

print("Name: Priti Paudel Jaisi, Roll_no: 10")
arr = list(map(int, input("Enter the elements (comma-separated): ").split(',')))

find_min_max(arr)
