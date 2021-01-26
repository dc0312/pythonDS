# Program to find maximum product of two integers in the array where all elements are positive
# Author : DC

import numpy as np


class MaxProduct:
    def getMaxProduct(self, arr):
        maxProduct = 0
        for i in range(0, len(myArr)):
            for j in range(i + 1, len(myArr)):
                if arr[i] * arr[j] > maxProduct:
                    maxProduct = arr[i] * arr[j]
        return maxProduct


if __name__ == '__main__':
    m = MaxProduct()
    myArr = np.array([1, 2, 3, 4, 3, 4, 5])
    print(m.getMaxProduct(myArr))
