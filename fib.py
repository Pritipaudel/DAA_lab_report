def fibonacci(n):
    a = 0
    b = 1
    if n == 0:
        return a
    elif n == 1:
        return b
    else:
        for _ in range(2, n+1):
            fib = a + b
            a = b
            b = fib
        return fib
print("Name:Priti Paudel Jaisi, Roll_no:10")
n=int(input("Enter the number: "))
print(f"Fibonacci number at position {n} is {fibonacci(n)}")
