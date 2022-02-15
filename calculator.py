from logo import logo
def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    return a / b


operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}

print(logo)
def calculator():
    should_continue = True
    num1 = float(input('what is first number: '))
    for symbol in operations:
        print(symbol)
    while should_continue:
        operation_symbol = input('pick an operation: ')
        num2 = float(input('what is the next number: '))
        answer = operations[operation_symbol](num1, num2)
        print(f'{num1} {operation_symbol} {num2} = {answer}')

        if input(f"type 'y' to continue calculating with {answer} or type 'n' to start new calculation.: ") == 'y':
            num1 = answer
        else:
            should_continue = False
            calculator()
calculator()
