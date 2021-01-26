# Program that accepts a number and adds up all the numbers from 0 to the number passed in the function
# Author : DC

class RecursiveRange:

    def getRecursiveRangeFunction(self, num):
        if num == 0:
            return 0
        return num + self.getRecursiveRangeFunction(num - 1);


if __name__ == '__main__':
    r = RecursiveRange()
    print(r.getRecursiveRangeFunction(10))
