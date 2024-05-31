def conv_num(num_str):
    """
    Takes a string in the form of decimal or hexadecimal
    Converts the strings to a base 10 number and returns it
    """

    first_char_zero_flag = False
    second_char_x_flag = False

    "Check to see if nothing was entered"
    if len(num_str) == 0:
        return None

    "Validate input prior to conversion"
    for char in range(0, len(num_str)):
        converted_char = ord(num_str[char])
        if converted_char <= 44:
            return None
        elif converted_char == 47:
            return None
        elif 58 <= converted_char <= 64:
            return None
        elif 71 <= converted_char <= 87:
            return None
        elif 89 <= converted_char <= 96:
            return None
        elif 103 <= converted_char <= 119:
            return None
        elif 121 <= converted_char:
            return None

    "Convert to the appropriate format"
    if first_char_zero_flag is True and second_char_x_flag is True:
        converted_num = convert_hex(num_str)
    else:
        converted_num = convert_decimal(num_str)

    return converted_num


def convert_hex(num_str):
    """
        Helper function use to convert a hexadecimal number to a base 10 number
        Returns the converted number
    """
    num_places = len(num_str) - 1
    sign_flag = False
    converted_hex = 0

    for char in range(0, len(num_str)):
        converted_char = ord(num_str[char])
        if converted_char == 48:  # Checks if the char is a zero
            num_places -= 1
        elif converted_char == 88 or converted_char == 120:  # Checks if the char is an upper or lowercase x
            num_places -= 1
        elif 49 <= converted_char <= 57:  # Checks if the char is a number
            converted_char -= 48
            converted_char *= pow(16, num_places)
            num_places -= 1
            converted_hex += converted_char
        elif 65 <= converted_char <= 70:  # Checks if the char is an uppercase letter
            converted_char -= 55
            converted_char *= pow(16, num_places)
            num_places -= 1
            converted_hex += converted_char
        elif 97 <= converted_char <= 102:  # Checks if the char is a lowercase letter
            converted_char -= 87
            converted_char *= pow(16, num_places)
            num_places -= 1
            converted_hex += converted_char
        else:
            sign_flag = True
            num_places -= 1

    if sign_flag is True:
        converted_hex *= -1

    return converted_hex


def convert_decimal(num_str):
    """
        Helper function use to convert a decimal number to a base 10 number
        Returns the converted number
    """
    num_places = len(num_str) - 1
    sign_flag = False
    converted_decimal = 0
    decimal_flag = False

    for char in range(0, len(num_str)):
        converted_char = ord(num_str[char])
        if 48 <= converted_char <= 57:  # Checks if the char is a number
            converted_char -= 48
            converted_char *= pow(10, num_places)
            converted_decimal += converted_char
            if decimal_flag is True:
                converted_decimal = round(converted_decimal,
                                          num_places * -1)  # Corrects rounding errors created by pow()
            num_places -= 1
        elif converted_char == 46:  # Checks if the char is a decimal point
            decimal_flag = True
            converted_decimal /= pow(10, num_places + 1)
            num_places = -1  # Corrects num_places for use with numbers after the decimal point
        else:
            sign_flag = True
            num_places -= 1

    if sign_flag is True:
        converted_decimal *= -1

    return converted_decimal
