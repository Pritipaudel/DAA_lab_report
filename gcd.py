def gcd(a, b):
    if a == 0:
        return b
    elif b == 0:
        return a

    while b != 0:
        r = a % b
        a = b
        b = r

    return a
print("Name:Priti Paudel Jaisi, Roll_no:10")
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

result = gcd(num1, num2)
print(f"The GCD of {num1} and {num2} is {result}.")
