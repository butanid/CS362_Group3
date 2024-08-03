def conv_num(num_str: str) -> float | None:
    converted_num: int | float = 0
    negative = False
    floating_point = False
    for char in num_str:
        if char == '-':
            negative = True
        elif char == '.':
            floating_point = True
        else:
            converted_num *= 10
            converted_num += (ord(char) - ord('0'))

    if negative:
        converted_num = -converted_num
    if floating_point:
        converted_num /= 100

    return converted_num
