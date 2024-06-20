# Problem
"""
Input:
- User enters the value x
- User enters the name of the activation function, which can only be one of three types (sigmoid, relu, elu)

Output: The result f(x) (x after passing through the corresponding activation function according to the activation function name). 
For example, if x=3 and activation_function='relu', Output: print 'relu: f(3)=3'

"""
import math
# Check if a given value is number
def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        return False

# activation-function   
def sigmoid(x):
    return 1 / (1 + math.exp(-x))

def relu(x):
    return max(0, x)

def elu(x, alpha=0.01):
    return x if x > 0 else alpha * (math.exp(x) - 1)


def activation_function(act_fn = input("Please enter the following functions (sigmoid, relu, elu): ").lower(),x = input("Enter the value x = ")):
    if not is_number(x):
        print("x must be a number")
        return
    
    x = float(x)

    if act_fn == "sigmoid":
        print(f"Sigmoid: f(x) = {sigmoid(x)}")
    elif act_fn == "relu":
        print(f"RELU: f(x) = {relu(x)}")
    elif act_fn == "elu":
        print(f"ELU: f(x) = {elu(x)}")
    else:
        print(f"{act_fn} is not supported")


# test
activation_function()  