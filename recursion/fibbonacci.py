# Program to find fibonacci series for a given number
# Author : DC

class Fibonacci:

    def getFibonacci(self, num):
        assert 0 <= num == int(num), "Please enter a valid number"
        if num in [0, 1]:
            return num;
        return self.getFibonacci(num - 1) + self.getFibonacci(num - 2)


if __name__ == '__main__':
    f = Fibonacci()
    print(f.getFibonacci(1))
