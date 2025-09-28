def power(n,b):
    if b == 0:
        return 1
    elif b == 1:
        return n
    else:
        b -= 1
        return n*power(n,b)

num = int(input("Input the number to find square of: "))
base = int(input("Enter the base: "))
print(power(num, base))