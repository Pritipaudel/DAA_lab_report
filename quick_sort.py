def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[0]
    less = [x for x in arr[1:] if x <= pivot]
    greater = [x for x in arr[1:] if x > pivot]
    return quick_sort(less) + [pivot] + quick_sort(greater)

print("Name: Priti Paudel Jaisi, Roll_no: 10")
arr = list(map(int, input("Enter the elements (comma-separated): ").split(',')))

arr = quick_sort(arr)
print("Sorted array:", arr)
