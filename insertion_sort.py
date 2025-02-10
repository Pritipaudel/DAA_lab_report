def insertion_sort(arr):
    n = len(arr)
    for i in range(1, n):
        temp = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > temp:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = temp

print("Name: Priti Paudel Jaisi, Roll_no: 62")
arr = list(map(int, input("Enter elements separated by commas: ").split(',')))

insertion_sort(arr)
print("Sorted array:", arr)
