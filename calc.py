import ast

def calculate_safe(expression):
    try:
        result = ast.literal_eval(expression)  # Only allows safe literals
        return result
    except (ValueError, SyntaxError):
        return "Invalid input"
