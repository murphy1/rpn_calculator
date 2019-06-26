# The main file for the project

"""
User will input an RPN expression, the program will calculate it and output the answer
The program will first push the numbers to the stack
It will then read the operator, pop the numbers, calculate the result and push that back to the stack
It will then read the next operator, pop the numbers, calculate the result and push it back to the stack
Will repeat until all operations are complete
Will then check for any print symbols and print the output if one is encountered

TO DO:

Manage exceptions

upload to github

write a README

add more comments

change variable names to be more readable

review code and update where needed

"""

from data_structures import Stack


class Operators:
# This class will handle the calculations for the program

    @staticmethod
    def operate(operator, num1, num2=0):

        # moved num2 in front for some of these expressions
        # this will help to give us the correct answer in cases like 3 4 - 5 +  which is (3-4) + 5 and 5 1 2 + 4 * + 3 -
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

        while len(expression) > self.COUNT:
            # Get the next item from the expression
            next_item = expression[self.COUNT]
            # count + 2, to skip the blank spaces
            self.COUNT += 2

            if next_item is "p":
                self.PRINT = True
            elif next_item not in self.operators:
                self.stack.push(next_item)
            else:
                num1 = int(self.stack.pop())
                if self.stack.is_empty() is False:
                    num2 = int(self.stack.pop())
                    result = Operators.operate(next_item, num1, num2)
                    self.stack.push(result)
                else:
                    result = Operators.operate(next_item, num1)
                    self.stack.push(result)

        if self.PRINT is True:
            print(self.stack.pop())
            # Reset the count and printing options so the method can be called again
            self.COUNT = 0
            self.PRINT = False
        else:
            self.COUNT = 0
            self.PRINT = False
            return self.stack.pop()

# stack [2,10]


#c = Calc()

#c.calculate("5 8 * n p")
#c.calculate("4 7 3 + + p")
#c.calculate("3 6 1 + + 2 e")
