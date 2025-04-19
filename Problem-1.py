class Calculator:
    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        if b == 0:
            return "Error: Cannot divide by zero."
        return a / b

    def calculate(self, a, b, operation):
        if operation == "add":
            return self.add(a, b)
        elif operation == "subtract":
            return self.subtract(a, b)
        elif operation == "multiply":
            return self.multiply(a, b)
        elif operation == "divide":
            return self.divide(a, b)
        else:
            return "Error: Invalid operation."

a = float(input())
b = float(input())
operation = input().lower()

calc = Calculator()
result = calc.calculate(a, b, operation)
print(result)

