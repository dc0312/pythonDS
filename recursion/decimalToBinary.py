# Program to find binary representation of decimal numbers
# Author : DC
class DecToBin:

    def getDecToBin(self, num):
        if int(num / 2) == 0:
            return num % 2
        return num%2 + 10 * self.getDecToBin(int(num / 2))


if __name__ == '__main__':
    d = DecToBin()
    print(d.getDecToBin(10))
