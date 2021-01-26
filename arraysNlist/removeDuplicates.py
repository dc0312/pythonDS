# Program to remove duplicates from the list
# Author : DC

class RemoveDuplicates:
    def removeDuplcates(self,arr):
        unique_list = list()

        for i in arr:
            if i not in unique_list:
                unique_list.append(i)

        return unique_list


if __name__ == '__main__':
    r = RemoveDuplicates()
    arr = [1,1,2,2,3,4,5]
    print(r.removeDuplcates(arr))

