def calculate(a, b, operator):
    if operator == "/":
        if b == 0:
            raise ValueError("Cannot divide by zero")
        return a / b