def main(input: str):

    expression = input.split()
    if len(expression) != 3:
        raise Exception("Вы ввели не два числа.")
    
    numb_1 = expression[0]
    numb_2 = expression[2]
    if numb_1.isdigit() and numb_2.isdigit():
        numb_1 = int(numb_1)
        numb_2 = int(numb_2)
    else:
        raise Exception("Введите целое число от 1 до 10")
    if not (1 <= numb_1 <= 10) or not (1 <= numb_2 <= 10):
        raise Exception("Введите целое число от 1 до 10")


    operator = expression[1]
    if operator == "+":
        result = numb_1 + numb_2
    elif operator == "-":
        result = numb_1 - numb_2
    elif operator == "*":
        result = numb_1 * numb_2
    elif operator == "/":
        result = numb_1 // numb_2
    else:
        raise Exception("Неверная операция")

    return str(result)
    
calculation = input("Введите два числа и оператор: ")
print(main(calculation))
