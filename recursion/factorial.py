# Program to find factorial of a number
# Author : DC

class FindFact:

    def factorial(self,num):
        assert int(num) == num and num >= 0, 'Please enter a correct number'
        if num in [0, 1]:
            return 1
        else:
            return num * self.factorial(num - 1)


if __name__ == '__main__':
    f = FindFact()
    print(f.factorial(5))
    # O/P --> 120
    # f = FindFact(-5)
    # print(f.factorial())
    # O/P
    #    assert int(self.num) == self.num and self.num >= 0, 'Please enter a correct number'
    # AssertionError: Please enter a correct number
    # f = FindFact('abc')
    # print(f.factorial())
    # O/P
    # assert int(self.num) == self.num and self.num >= 0, 'Please enter a correct number'
    # ValueError: invalid literal for int() with base 10: 'abc'
