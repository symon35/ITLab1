def add_in_base(a: str, b: str, base: int) -> str:
    if not (2 <= base <= 36):
        raise ValueError("Основание системы счисления должно быть от 2 до 36")

    def char_to_int(c):
        if '0' <= c <= '9':
            return ord(c) - ord('0')
        elif 'A' <= c <= 'Z':
            return ord(c) - ord('A') + 10
        elif 'a' <= c <= 'z':
            return ord(c) - ord('a') + 10
        else:
            raise ValueError(f"Недопустимый символ: {c}")

    def int_to_char(n):
        if 0 <= n <= 9:
            return chr(ord('0') + n)
        else:
            return chr(ord('A') + n - 10)

    # Проверка символов и преобразование в список цифр
    digits_a = []
    for char in a:
        val = char_to_int(char)
        if val >= base:
            raise ValueError(f"Цифра {char} недопустима для основания {base}")
        digits_a.append(val)

    digits_b = []
    for char in b:
        val = char_to_int(char)
        if val >= base:
            raise ValueError(f"Цифра {char} недопустима для основания {base}")
        digits_b.append(val)

    # Выравнивание длины
    max_len = max(len(digits_a), len(digits_b))
    digits_a = [0] * (max_len - len(digits_a)) + digits_a
    digits_b = [0] * (max_len - len(digits_b)) + digits_b

    # Сложение столбиком
    result = []
    carry = 0
    for i in range(max_len - 1, -1, -1):
        total = digits_a[i] + digits_b[i] + carry
        result.append(total % base)
        carry = total // base

    if carry > 0:
        result.append(carry)

    # Формирование строки результата
    result_str = ''.join(int_to_char(d) for d in reversed(result))
    
    # Удаление ведущих нулей
    result_str = result_str.lstrip('0')
    return result_str if result_str != '' else '0'
