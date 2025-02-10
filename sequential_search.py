def sequential_search(a, key):
    for i in range(len(a)):
        if a[i] == key:
            print("Successful")
            return
    print("Failed")

print("Name: Priti Paudel Jaisi, Roll_no: 10")
arr = list(map(int, input("Enter the elements (comma-separated): ").split(',')))
key = int(input("Enter the element to search for: "))

sequential_search(arr, key)
