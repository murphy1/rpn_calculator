# rpn_calculator
Reverse Polish Notation Calculator

User will input an RPN expression, the program will calculate it and output the answer.

How it works:
The program will loop through the expression. If there is a number, it will be pushed to the stack.
If the program reads an operator, it will pop the numbers, calculate the result and push that result back to the stack.
It will then read the next operator and repeat the above step.
Will repeat until all operations are complete.
Will then check for a print symbol and print the output if one is encountered.
