def selection_sort(arr):
    n = len(arr)
    for i in range(n - 1):
        min_index = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        if min_index != i:
            arr[i], arr[min_index] = arr[min_index], arr[i]

print("Name: Priti Paudel Jaisi, Roll_no: 10")
arr = list(map(int, input("Enter elements separated by commas: ").split(',')))

selection_sort(arr)
print("Sorted array:", arr)
