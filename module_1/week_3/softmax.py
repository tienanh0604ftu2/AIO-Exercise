"""
In this section, we build the Softmax class and the softmax_stable class, 
which take a 1-dimensional array (1-dimensional tensor) as input based on 
inheritance from the Module class and override the forward() method
"""

import math

class Softmax:
    def __init__(self):
        # No initialization required for this class
        pass

    def softmax(self,lst):
        exp_lst = [math.exp(x) for x in lst]
        total_lst = sum(exp_lst)
        return [round(x/total_lst,4) for x in exp_lst]
    

class SoftmaxStable(Softmax):
    def __init__(self):
        super().__init__()

    def softmax_stable(self,lst):
        max_value = max(lst)
        subtract_lst =  [(x - max_value) for x in lst]
        exp_lst = [math.exp(x) for x in subtract_lst]
        total_lst = sum(exp_lst)
        return [round(x/total_lst,4) for x in exp_lst]
    
# test case
x = [1,2,3]
softmax_stable = SoftmaxStable()
output1 = softmax_stable.softmax(x)
output2 = softmax_stable.softmax_stable(x)

print(output1)
print(output2)