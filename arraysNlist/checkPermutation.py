# Program to check if two strings are permutation or not
# Author : DC

class CheckPermutation:

    def isPermuation(self, str1, str2):
        str1_list = list(str1.lower())
        str2_list = list(str2.lower())
        print(str1_list)
        print(str2_list)
        if len(str1) != len(str2):
            return False
        for s in str1_list:
            if s in str2_list:
                str2_list.remove(s)
        print(str2_list)
        if len(str2_list) == 0:
            return True
        else:
            return False


if __name__ == '__main__':
    c = CheckPermutation()
    string1 = "Deepak"
    string12 = "Keeedp"
    print(c.isPermuation(string1, string12))
