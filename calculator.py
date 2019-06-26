# The main file for the project. Contains the Operators and Calculation class

from data_structures import Stack


class Operators:
    """This class will handle the calculations for the program"""

    @staticmethod
    def operate(operator, num1, num2=0):
        if operator is "+":
            return num2 + num1
        elif operator is "-":
            return num2 - num1
        elif operator is "*":
            return num2 * num1
        elif operator is "//":
            return num2 // num1

        # For unary operators like below we will only pop one element to be calculated
        elif operator is "n":
            return num1 * -1

        elif operator is "e":
            return num2 ** num1


class Calc:

    COUNT = 0
    # If there is a 'p' at the end of the expression. This will set to True and print the result
    PRINT = False

    def __init__(self):
        self.stack = Stack()
        self.COUNT = 0
        self.PRINT = False
        self.operators = ["+", "-", "*", "//", "n", "e"]

    def calculate(self, expression):
        # loop through the expression
        while len(expression) > self.COUNT:
            # Get the next item from the expression
            next_item = expression[self.COUNT]
            # count + 2, to skip the blank spaces
            self.COUNT += 2

            if next_item is "p":
                self.PRINT = True

            # add the numbers to the stack
            elif next_item not in self.operators:
                self.stack.push(next_item)

            else:
                # if and operator is found, pop the numbers
                num1 = int(self.stack.pop())
                if self.stack.is_empty() is False:
                    num2 = int(self.stack.pop())
                    # send to the calculation class and get the result
                    result = Operators.operate(next_item, num1, num2)
                    # push the result to the stack
                    self.stack.push(result)
                else:
                    result = Operators.operate(next_item, num1)
                    self.stack.push(result)

        # if a print symbol is found. Print result to the terminal
        if self.PRINT is True:
            print(self.stack.pop())
            # Reset the count and printing options so the method can be called again
            self.COUNT = 0
            self.PRINT = False
        else:
            self.COUNT = 0
            self.PRINT = False
            return self.stack.pop()
