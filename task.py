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

def conv_endian(num, endian='big'):
    """Function takes in an integer value, converts it to a hexadecimal number, and returns it as a string"""
    # String of hexadecimal numbers
    hex_digits = "0123456789ABCDEF"
    # Variable to store output
    hex_string = ""

    # Checks if valid endian
    if endian not in ('big', 'little'):
        return None

    # Variable for negative numbers
    negative_num = num < 0
    # Checks if num is negative
    if negative_num:
        num = abs(num)

    # Checks if integer value is 0
    if num == 0:
        hex_string = "0"
    else:
        while num > 0:
            # Convert integer value to hexadecimal
            hex_string = hex_digits[num % 16] + hex_string
            num = num // 16

    # Checks if hex string is odd
    if len(hex_string) % 2 != 0:
        # Adding 0 to front of string for even characters
        hex_string = '0' + hex_string

    # Variable to store byte pairs
    byte_pairs = []
    # Loop through hex string values
    for i in range(0, len(hex_string), 2):
        # Split hex string into byte pairs and append to list
        byte_pairs.append(hex_string[i:i+2])

    # Checking if value of 'big' endian
    if endian == 'big':
        result = " ".join(byte_pairs)
    # Checking if value of 'little' endian
    else:
        # Reverse list of byte pairs for little endian
        byte_pairs.reverse()
        result = " ".join(byte_pairs)

    # Checks if num is negative
    if negative_num:
        # Adding negative symbol to front of string
        result = '-' + result

    return result
