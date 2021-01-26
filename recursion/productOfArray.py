# Program to find product of an array
# Author : DC

class ProductOfArray:

    def getProductOfArray(self, arr):
        if len(arr) == 1:
            return arr[0]
        return arr[0] * self.getProductOfArray(arr[1:])


if __name__ == '__main__':
    p = ProductOfArray()
    print(p.getProductOfArray([1, 2, 3,4]))
