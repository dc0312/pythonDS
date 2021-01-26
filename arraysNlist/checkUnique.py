# Program to find a list that has all unique characters or not
# Author : DC

class UniqueList:

    def isUniqueList(self, checkList):
        my_list = list()
        for i in checkList:
            if i not in my_list:
                my_list.append(i)
            else:
                return False
        return True


if __name__ == '__main__':
    u = UniqueList()
    checkList = [1, 2, 3, 5,3]
    print(u.isUniqueList(checkList))
