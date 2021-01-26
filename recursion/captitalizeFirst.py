# Program to capitalize the first letter of each string in the array
# Author : DC

class CapitalizeFirst:

    def capitalizeFirst(self, arr):
        resultArr = []
        if len(arr) == 0:
            return resultArr
        resultArr.append(arr[0][0].upper() + arr[0][1:])
        return resultArr + self.capitalizeFirst(arr[1:])


if __name__ == '__main__':
    c = CapitalizeFirst()
    print(c.capitalizeFirst(['car', 'dog', 'banana']))
    arr = [1, 2, 3]
    arr.append(4)
    print(arr)
    print(arr + [5, 6])
