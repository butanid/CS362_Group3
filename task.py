def my_datetime(num_sec):
    """Function 2: takes num_sec and converts it to a date and returns it as a
    string with the following format MM-DD-YYYY."""
    # Constants for seconds per day by 24*60*60= 86400.
    seconds_per_day = 86400

    # Leap year check, such as 2000 or 2400 is leap year.
    def is_leap_year(year):
        if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
            return True
        return False

    # Calculate total days since epoch "01-01-1970".
    total_days = num_sec // seconds_per_day

    # Start from January 1, 1970.
    year = 1970
    while True:
        current_year_days = 366 if is_leap_year(year) else 365
        if total_days < current_year_days:
            break
        total_days -= current_year_days
        year += 1

    # Determine the month and day in the final year.
    month_lengths = [31, 28 + is_leap_year(year), 31, 30, 31, 30, 31, 31,
                     30, 31, 30, 31]
    month = 0
    while total_days >= month_lengths[month]:
        total_days -= month_lengths[month]
        month += 1

    # Formatting the date string
    month += 1  # to make the month 1-indexed.
    day = total_days + 1  # to make the day 1-indexed.
    return f'{month:02d}-{day:02d}-{year}'


def conv_num(num_str):
    """This function takes a string and converts it into a
    base 10 number and returns it
    """

    if not isinstance(num_str, str) or len(num_str) == 0:
        return None

    # check if string contains at least one digit
    if not any(char.isdigit() for char in num_str):
        return None

    # Check for multiple '-' and misplaced '-'
    if num_str.count('-') > 1 or (num_str.count('-') == 1 and num_str[0] != '-'):
        return None

    num_str = num_str.strip()
    num_str = num_str.lower()
    negative = False
    converted_num = 0

    # if the argument is a hexadecimal number,
    # convert it to a base 10 number.
    if num_str.startswith('0x') or num_str.startswith('-0x'):

        converted_num = conv_hex_num(num_str)

    # If not a hex digit, check for floating point number
    elif num_str.count('.') == 1:
        converted_num = conv_floating_num(num_str)

    # Check for an int.
    else:
        for char in num_str:
            if char == '-':
                negative = True
            elif char.isdigit():
                converted_num *= 10
                converted_num += (ord(char) - ord('0'))
            else:
                return None

    if negative:
        converted_num = -converted_num

    return converted_num


def conv_hex_num(hex_str):
    """Converts a hex string to a decimal number and returns it"""

    converted_hex = 0
    negative = False
    hex_str = hex_str.replace('0x', '')
    hex_num_len = len(hex_str) - 1
    hex_dictionary = {'0': 0, '1': 1, '2': 2, '3': 3,
                      '4': 4, '5': 5, '6': 6, '7': 7,
                      '8': 8, '9': 9, 'a': 10, 'b': 11,
                      'c': 12, 'd': 13, 'e': 14, 'f': 15}

    for char in hex_str:
        if char == '-':
            negative = True
            hex_num_len -= 1
        elif char in hex_dictionary:
            converted_hex = converted_hex + \
                hex_dictionary[char] * 16 ** hex_num_len
            hex_num_len -= 1
        else:
            return None
    if negative:
        return -converted_hex
    return converted_hex


def conv_floating_num(floating_num_str):
    """Converts floating point string to floating point number and returns it"""

    decimal_point = floating_num_str.find('.') + 1
    num_len = len(floating_num_str)
    floating_num_str = floating_num_str.replace('.', '')
    converted_float = 0
    negative = False

    for char in floating_num_str:
        if char == '-':
            negative = True
        elif char.isdigit():
            converted_float *= 10
            converted_float += (ord(char) - ord('0'))
        else:
            return None

    power = 10 ** (num_len - decimal_point)
    converted_float /= power

    if negative:
        return -converted_float

    return converted_float
