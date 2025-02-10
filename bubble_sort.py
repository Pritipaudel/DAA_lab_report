def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]  
    return arr
print("Name: Priti Paudel Jaisi, Roll_no:10")
arr = list(map(int, input("Enter the elements (comma-separated): ").split(',')))
sorted_arr = bubble_sort(arr)
print("Sorted array:", sorted_arr)
