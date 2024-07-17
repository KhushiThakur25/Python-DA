# 1. try - logic
# 2. except - error
# 3. else - option
# 4. finally - I'm always executed..

try:
    n = int(input("Enter the value of n"))
    m = int(input("Enter the value of m"))

    add = n + m
    sub = n - m
    mul = n * m
    div = n / m
except ValueError as msg:
    print(msg)
except ZeroDivisionError:
    print("Zero value can't divide the value.")
except Exception as msg:
    print(msg)
else:
    print("sum is",add)
    print("sub is",sub)
    print("mul is",mul)
    print("div is",div)
finally:
    print("I'm always executed...")


