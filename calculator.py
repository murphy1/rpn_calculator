# The main file for the project. Contains the Helper and Calculation class

from data_structures import Stack


class Helper:
    """This helper class will format the expression and handle the calculations"""

    def __init__(self):
        self.operators = ["+", "-", "*", "//", "n", "e", "p"]

    def format_expression(self, expression):
        result = ""
        for char in expression:
            if char.isdigit() or char in self.operators:
                result += char+" "
        return result

    @staticmethod
    def get_result(operator, num1, num2=0):
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
        self.form = Helper()

    def calculate(self, unformatted_expression):
        # format the expression correctly so it can be calculated
        expression = self.form.format_expression(unformatted_expression)

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
                # if an operator is found, pop the numbers
                try:
                    num1 = int(self.stack.pop())
                    if self.stack.is_empty() is False:
                        num2 = int(self.stack.pop())
                        # send to the calculation class and get the result
                        result = Helper.get_result(next_item, num1, num2)
                        # push the result to the stack
                        self.stack.push(result)
                    else:
                        result = Helper.get_result(next_item, num1)
                        self.stack.push(result)
                except ValueError:
                    print("Cannot calculate. Invalid Expression!")
                    return

        # if a print symbol is found. Print result to the terminal
        try:
            if self.stack.is_empty():
                raise ValueError
            if self.PRINT is True:
                print(self.stack.pop())
                # Reset the count and printing options so the method can be called again
                self.COUNT = 0
                self.PRINT = False
            else:
                self.COUNT = 0
                self.PRINT = False
                return self.stack.pop()
        except ValueError:
            print("Cannot calculate. Invalid Expression!")
            return
