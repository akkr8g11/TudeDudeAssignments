def factorial(n):
    if n == 0:
        return 1
    else:
        return n*factorial(n-1)

#Driver Code    
n = input("Enter a number: ")
print(f"Factorial of {n} is {factorial(int(n))}")