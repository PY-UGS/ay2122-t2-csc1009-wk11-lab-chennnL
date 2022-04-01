# calculator class
class calculator:

    # constructor
    # @param x - first number input
    # @param y - second number input
    def __init__(self, x, y):
        self.x = x
        self.y = y

    # function to sum x and y
    def adder(self):
        z = int(self.x) + int(self.y)
        print("The sum of", self.x, "and", self.y, "is", z)

    # function to subtract x and y
    def subtractor(self):
        z = int(self.x) - int(self.y)
        print("The difference of", self.x, "and", self.y, "is", z)

    # function to multiply x and y
    def multiplier(self):
        z = int(self.x) * int(self.y)
        print("The multiple of", self.x, "and", self.y, "is", z)

    # function to divide x and y
    def divider(self):
        try:
            z = int(self.x) / int(self.y)
            print("The quotient of", self.x, "and", self.y, "is", z)
        # handle zero division exception
        except ZeroDivisionError:
            print("Divisor cannot be zero")

    # function to set x and y to zero
    def clear(self):
        x = 0
        y = 0
        self.x = x
        self.y = y
        print("The first number is:", x)
        print("The second number is:", y)

def main():
    # get user to input 2 numbers
    x = int(input("Enter first number: "))
    y = int(input("Enter second number: "))

    # create calculator object
    result = calculator(x, y)
    # perform functions to the object
    result.adder()
    result.subtractor()
    result.multiplier()
    result.divider()
    result.clear()

main()

