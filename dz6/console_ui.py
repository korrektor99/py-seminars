def view_data(data, title):
    print(f'{title} = {data}')


def get_value():
    return input()


def input_data():
    print(' Введите 1 для работы с комплексными числами, 2 - для работы с рациональными числами')
    data_type = get_value()
    if data_type == '1':
        print('Введите первое число (используйте формат: "10+5j"):')
        left_value = get_value()
        print('Введите второе число (используйте формат: "10+5j"):')
        right_value = get_value()
        print('Выберите знак по типу "+" "-" "*" "/" ')
        oper = get_value()
    elif data_type == '2':
        print('Введите первое число (используйте формат: "1/123"):')
        left_value = get_value()
        print('Введите второе число (используйте формат: "1/123"):')
        right_value = get_value()
        print('Выберите знак по типу "+" "-" "*" "/" ')
        oper = get_value()
    return (data_type, left_value, oper, right_value)