class Calculator:
    def operate(self, a: float, b: float, operation: str):
        if operation == "add":
            return a + b
        elif operation == "subtract":
            return a - b
        elif operation == "multiply":
            return a * b
        elif operation == "divide":
            return a / b if b != 0 else "Cannot divide by zero"
        else:
            return "Invalid operation"

a = float(input("Enter first number (a): "))
b = float(input("Enter second number (b): "))
operation = input("Enter operation (add / subtract / multiply / divide): ").strip().lower()


calc = Calculator()
result = calc.operate(a, b, operation)

print("Result:", result)