# Program to find power of a given number
# Author : DC
class Power:

    def getPower(self, num, power):
        assert 0 <= num == int(num), " Please use positive numbers only"
        if power == 0:
            return 1
        return num * self.getPower(num, power - 1)


if __name__ == '__main__':
    p = Power()
    print(p.getPower(-1, 3))
