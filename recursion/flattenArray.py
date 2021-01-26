# Program to check if a given string is palindrome or not
# Author : DC

class FlattenArray:

    def flatten(self, arr):
        result_arr = [];

        for custItem in arr:
            if type(custItem) is list:
                result_arr.extend(self.flatten(custItem))
            else:
                result_arr.append(custItem)

        return result_arr


if __name__ == '__main__':
    f = FlattenArray()
    print(f.flatten([1, 2, 3,[4, [[5]]]]))
