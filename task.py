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


def conv_num(num_str) -> float | None:

    if not isinstance(num_str, str):
        return None

    if len(num_str) == 0:
        return None

    num_str = num_str.strip()
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

    print(converted_num)

    return converted_num
