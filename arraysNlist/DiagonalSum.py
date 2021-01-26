# Program to find of sum of diagonal of a 2D Array
# Author : DC

class DiagonalSum:

    def getSum(self,arr):
        rows = len(arr)
        sum = 0
        for i in range(0,rows):
            sum += arr[i][i]

        return sum



if __name__ == '__main__':
    d = DiagonalSum()
    two_d_arr = [[1,2,3],[4,5,6],[7,8,9]]
    print(two_d_arr)
    print(d.getSum(two_d_arr))
