# Program to check if a given string is palindrome or not
# Author : DC

class Palindrome:

    def isPalindrome(self, string):
        string = string.lower()
        if len(string) == 0:
            return True
        elif string[0] != string[len(string) - 1]:
            return False
        else:
            return self.isPalindrome(string[1:len(string) - 1])
            # return self.isPalindrome(string[1:-1])


if __name__ == '__main__':
    p = Palindrome()
    print(p.isPalindrome("Maam"))
