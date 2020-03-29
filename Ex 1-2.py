def calculate(o, a, b):
    try:
        assert o in ['+', '-', '*', '/'], 'Операция недоступна'
        if o == "+":
            result = a + b
        if o == "-":
            result = a - b
        if o == "*":
            result = a * b
        if o == "/":
            result = a / b
        print(result)
    except AssertionError:
        print('Операция недоступна')
    except ZeroDivisionError:
        print('На ноль делить нельзя')


def main():
    while True:
        print('Введите оператор (+, -, *, /) и два положительных числа')
        try:
            o, a, b = input().split()
            a, b = [int(a), int(b)]
            calculate(o, a, b)
        except ValueError as e:
            print(e)


main()
