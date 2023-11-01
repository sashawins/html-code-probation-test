# Бонус-Задание 2 (Python3)


def rearrange_to_max(num):
    str_num = str(num)
    digits = list(str_num)
    digits.sort(reverse=True)
    max_num = int("".join(digits))

    return max_num


n = int(input("Введите значение: "))
print("Полученное число:", rearrange_to_max(n))
