iternal = "y"

while iternal == "y":
    first_num = float(input("Введите число:"))
    operator = input("Выберите оператор:")
    last_num = float(input("Введите второе число:"))
    if operator == "+":
        print(first_num + last_num)
    elif operator == "-":
        print(first_num - last_num)
    elif operator == "*":
        print(first_num * last_num)
    elif operator == "/":
        print(first_num / last_num)
    else:
        print("Проверьте корректность введённых данных")
    iternal = input("Нажмите y, чтобы продолжить или любую клавишу, чтобы завершить работу")