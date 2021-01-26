# Program to find a missing number in a given range
# Author : DC

class MissingNumber:

    def getMissingNumber(self, numList):
        max_number = max(numList)
        sum = 0
        for i in range(1, max_number + 1):
            sum += i

        sumList = 0
        for i in numList:
            sumList += i

        return sum - sumList


if __name__ == '__main__':
    m = MissingNumber()
    a = [1, 2, 3, 5, 6, 7, 8, 9, 10]

    missing_number = m.getMissingNumber(a)
    print("Missing Number : " + str(missing_number))
