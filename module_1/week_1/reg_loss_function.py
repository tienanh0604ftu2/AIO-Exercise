import random
import math

"""
Input:
– The user enters the number of samples (num_samples) to be generated (only accepts integer numbers).
– The user enters the loss name (MAE, MSE, RMSE-(optional)). Only MAE and MSE are required; anyone who wants to include RMSE can do so.
• Output: Print the loss name, sample, predict, target, loss.

"""

# reg loss function


def mae(y, y_hat):
    return abs(y - y_hat)


def mse(y, y_hat):
    return (y - y_hat) ** 2


def rmse(y, y_hat):
    return (y - y_hat) ** 2


def reg_loss_func(num_sample=input("Enter the number of sample: "), loss_func=input("Enter the name of loss function (mae, mse, rmse): ").lower()):
    try:
        int(num_sample)
    except ValueError:
        print("num_sample must be integer")
        return
    num_sample = int(num_sample)
    loss_func_list = ["mae", "mse", "rmse"]

    if loss_func not in loss_func_list:
        print(f"{loss_func} is not supported")

    loss_values = []

    if loss_func == "mae":
        for _ in range(num_sample):
            y = random.uniform(0, 10)
            y_hat = random.uniform(0, 10)
            loss_values.append(mae(y, y_hat))
        print(f"The value of mae is {sum(loss_values)/num_sample}")

    if loss_func == "mse":
        for _ in range(num_sample):
            y = random.uniform(0, 10)
            y_hat = random.uniform(0, 10)
            loss_values.append(mse(y, y_hat))
        print(f"The value of mse is {sum(loss_values)/num_sample}")

    if loss_func == "rmae":
        for _ in range(num_sample):
            y = random.uniform(0, 10)
            y_hat = random.uniform(0, 10)
            loss_values.append(rmse(y, y_hat))
        result = (sum(loss_values)/num_sample) ** 0.5
        print(f"The value of rmse is {result}")


reg_loss_func()
