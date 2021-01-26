# Program to get first and second best scores from the list
# Author : DC

class TopTwo:

    def getTopTwo(self, arr):
        first = 0
        second = 0

        for i in arr:
            if i > second:
                second = i
            if second > first:
                second = first
                first = i
        print( str(first) + " " + str(second))


if __name__ == '__main__':
    t = TopTwo()
    myList = [10, 11, 13, 15, 12, 20, 18, 20, 40, 35]
    t.getTopTwo(myList)
