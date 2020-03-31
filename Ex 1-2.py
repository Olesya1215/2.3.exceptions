def calculate(operator, operand1, operand2):
    assert operator in ['+', '-', '*', '/'], 'Операция недоступна'
    assert operand1 > 0 and operand2 > 0, 'Введите два положительных числа'
    try:
        if operator == "+":
            result = operand1 + operand2
        if operator == "-":
            result = operand1 - operand2
        if operator == "*":
            result = operand1 * operand2
        if operator == "/":
            result = operand1 / operand2
        print(result)
    except AssertionError:
        print('Операция недоступна')
    except ZeroDivisionError:
        print('На ноль делить нельзя')


def main():
    while True:
        print('Введите оператор (+, -, *, /) и два положительных числа')
        try:
            operator, operand1, operand2 = input().split()
            operand1, operand2 = [int(operand1), int(operand2)]
            calculate(operator, operand1, operand2)
        except ValueError as e:
            print(e)


main()
