# Program to reverse a given string
# Author : DC
class ReverseString:

    # def reverse(self, str):
    #     if len(str) == 1:
    #         return str
    #     return str[len(str) - 1] + self.reverse(str[:len(str) - 1])

    def reverse(self, str):
        if str == '':
            return ''
        return self.reverse(str[1:]) + str[0]


if __name__ == '__main__':
    r = ReverseString()

    print(r.reverse("Deepak"))
