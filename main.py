from random import randint

'''
Игра "Быки и коровы".
Цель игры - найти загаданную последовательность трёх цифр.
Цифры не должны повторяться.
Дается 5 попыток.
+ - если цифра есть и стоит на своем месте
● - если цифра есть, но стоит не на своём месте
- - цифры нет
'''


def secret_number():
    # Генерируем секретное число.
    secret = '0'
    while len(set(secret)) != 3:
        secret = list(str(randint(102, 987)))
    return secret


def input_number(secret_num):
    # Считываем число, введенное пользователем
    print(
        '\033[1;30;42m  Игра "Быки и коровы"  \033[0m\n'
        'Цель игры - найти загаданную последовательность из трёх цифр.\n'
        'Цифры не должны повторяться.\n'
        'У вас есть 5 попыток.\n'
        '+ - если цифра есть и стоит на своем месте\n'
        '● - если цифра есть, но стоит не на своём месте\n'
        '- - цифры нет\n'
    )
    result = []
    cnt_move = 1
    while result != ['+', '+', '+']:
        if cnt_move == 5:
            print('\033[31mУ вас осталась одна попытка. \033[0m')
        user_num = input('Введите трехзначное число: ')
        # Проверяем, чтобы цифры в числе не повторялись
        while not user_num.isdigit() or len(set(user_num)) != 3:
            print('Неправильный ввод. Попробуйте еще раз.')
            user_num = input('Введите трехзначное число: ')

        # Разбиваем оба числа на три цифры
        user_num = list(user_num)
        for i in range(3):
            if user_num[i] == secret_num[i]:
                result.append('+')
            elif user_num[i] in secret_num:
                result.append('●')
            else:
                result.append('-')
        if result == ['+', '+', '+']:
            secret_num = ''.join(secret_num)
            print(*user_num)
            print(*result)
            print(f'\033[32mПоздравляю, вы победили!\nЗагаданное число - {secret_num}.\033[0m')
            break
        elif cnt_move == 5:
            secret_num = ''.join(secret_num)
            print(f'\033[31mВы проиграли.\nЗагаданное число - {secret_num}.\033[0m')
            break
        print(*user_num)
        print(*result)
        cnt_move += 1
        result.clear()


if __name__ == '__main__':
    num = secret_number()
    input_number(num)
