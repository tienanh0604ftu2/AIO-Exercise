# compute factorial

def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n-1)


"""
Please pay attention to the following conditions
• x is in radians
• n is a positive integer > 0
"""


def approximate_func(x=input("Enter the value of x: "), n=input("Enter the value of n: "), app_func=input("Select the function (sin, cos, sinh, cosh): ").lower()):
    # x
    try:
        float(x)
    except ValueError:
        print("x must be a number")
        return
    x = float(x)

    # n
    try:
        int(n)
    except ValueError:
        print("n must be integer")
        return
    n = int(n)
    if n < 0:
        print("n must be greater than zero")
        return

    app_func_list = ["sin", "cos", "sinh", "cosh"]
    if app_func not in app_func_list:
        print(f"{app_func} is not supported")

    result = 0
    for i in range(n):
        if app_func == "sin":
            result += (-1) ** i * (x ** (2 * i + 1) / (factorial(2 * i + 1)))
        elif app_func == "cos":
            result += (-1) ** i * (x ** (2 * i) / (factorial(2 * i)))
        elif app_func == "sinh":
            result += x ** (2 * i + 1) / (factorial(2 * i + 1))
        elif app_func == "cosh":
            result += x ** (2 * i) / (factorial(2 * i))
    print(f"The value of approximate function {app_func} is {result}")


approximate_func()
