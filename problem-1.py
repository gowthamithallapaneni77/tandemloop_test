
# problem 1 : small calculator 


class Calculator:
    def __init__(self, a, b):
        self.a = float(a)
        self.b = float(b)

    def operate(self, operation):
        op = operation.lower()
        if op == "add":
            return self.a + self.b
        elif op == "sub":
            return self.a - self.b
        elif op == "mul":
            return self.a * self.b
        elif op == "div":
            if self.b != 0:
                return self.a / self.b
            else:
                return "Error: Division by zero"
        else:
            return "Invalid operation"

a = float(input("Enter first number (a): "))
b = float(input("Enter second number (b): "))
operation = input("Enter operation (add/sub/mul/div): ")

calc = Calculator(a, b)
result = calc.operate(operation) 
print("Result:",result)