# Calculate Mean Difference of nth Root Error
"""
n: nth root
p: nth of loss function
"""


def md_nre(y, y_hat, n, p):
    parameters = [y, y_hat, n, p]
    for para in parameters:
        try:
            float(para)
        except ValueError:
            print(f"{para} must be a number")
            return
    return (y**(1/n)-y_hat**(1/n))**p


# test
print(md_nre(100, 99.5, 2, 1))
