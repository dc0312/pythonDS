# Program to find sum of digits
# Author : DC
class SumOfDigits:

    def getSumOfDigits(self, num):
        assert 0 <= num == int(num), "Please use a positive number"
        if num == 0:
            return 0
        return int(num % 10) + self.getSumOfDigits(int(num / 10))


if __name__ == '__main__':
    s = SumOfDigits()
    print(s.getSumOfDigits(123))
