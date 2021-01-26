# Program to find gcd of two numbers
# Author : DC
class GCD:

    def getGCD(self, num1, num2):

        if num2 == 0:
            return num1
        else:
            return self.getGCD(num2, num1 % num2)


if __name__ == '__main__':
    g = GCD()
    print(g.getGCD(12, 48))
