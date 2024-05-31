def conv_num(num_str):
    """
    Takes a string in the form of decimal or hexadecimal
    Converts the strings to a base 10 number and returns it
    """
    sign_flag = False
    first_char_zero_flag = False
    second_char_x_flag = False
    decimal_flag = False

    "Check to see if nothing was entered"
    if len(num_str) == 0:
        return None

    "Validate input prior to conversion"
    for char in range(0, len(num_str)):
        converted_char = ord(num_str[char])
        if char == 0 and converted_char == 45:  # Checks if the first char is a minus sign
            sign_flag = True
        elif converted_char == 46:  # Checks if the char is a decimal point
            decimal_flag = is_decimal(converted_char, second_char_x_flag, decimal_flag)
            if decimal_flag is None:
                return None
        elif 48 <= converted_char <= 57:  # Checks if the char is a number
            first_char_zero_flag = is_decimal(converted_char,second_char_x_flag, decimal_flag)
        elif 65 <= converted_char <= 70:  # Checks if the char is an uppercase letter
            if first_char_zero_flag is False or second_char_x_flag is False:
                return None
        elif 97 <= converted_char <= 102:  # Checks if the char is a lowercase letter
            if first_char_zero_flag is False or second_char_x_flag is False:
                return None
        elif converted_char == 88 or converted_char == 120:  # Checks if the char is an upper or lowercase x
            second_char_x_flag = is_x(char, converted_char, decimal_flag, sign_flag)
            if second_char_x_flag is None:
                return None
        else:
            return None

    "Convert to the appropriate format"
    if first_char_zero_flag is True and second_char_x_flag is True:
        converted_num = convert_hex(num_str)
    else:
        converted_num = convert_decimal(num_str)

    return converted_num


def is_minus_sign(char, converted_char):

    if char == 0 and converted_char == 45:  # Checks if the first char is a minus sign
        return True
    return False


def is_number(char, converted_char, sign_flag):

    if sign_flag is True and char == 1 and converted_char == 48:
        return True
    elif char == 0 and converted_char == 48:
        return True


def is_decimal(converted_char, x_flag, decimal_flag):

    if converted_char == 46:  # Checks if the char is a decimal point
        if x_flag is True:
            return None
        elif decimal_flag is False:
            return True


def is_hex_letter(converted_char, zero_flag, x_flag):
    if 65 <= converted_char <= 70:  # Checks if the char is an uppercase letter
        if zero_flag is False or x_flag is False:
            return None
    elif 97 <= converted_char <= 102:  # Checks if the char is a lowercase letter
        if zero_flag is False or x_flag is False:
            return None
    return True


def is_x(char, converted_char, decimal_flag, sign_flag):

    if converted_char == 88 or converted_char == 120:  # Checks if the char is an upper or lowercase x
        if decimal_flag is True:
            return None
        elif sign_flag is True and char == 2:
            return True
        elif char == 1:
            return True
        else:
            return None


def is_valid(converted_char):
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
    return True


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


if __name__ == '__main__':
    print(convert_decimal("394.6"))
    print(convert_decimal("32394.6"))
    print(convert_decimal("32394.64"))
    # Gets weird if a zero is in-between numbers
    print(convert_decimal("323904.645"))
    print(conv_num('12345'))
    print(conv_num('-123.45'))
    print(conv_num('.45'))
    print(conv_num('123.'))
    print(conv_num('0xAD4'))
    print(conv_num('0Xad4'))
    print(conv_num('0xAZ4'))

    "Tests"
    print("")
    print("Tests")
    print(conv_num(''))
    print(conv_num(' '))
    print(conv_num(' 12345'))
    print(conv_num('0x AD4'))
    print(conv_num('12345 '))
    print(conv_num('12.3.45'))
    print(conv_num('0xFF.02'))
    print(conv_num('-0xAD4-'))
    "Valid"
    print(conv_num('.45'))
    "Valid"
    print(conv_num('123.'))
    print(conv_num('12345A'))
    print(conv_num('12345a'))
    print(conv_num('0xAg4'))
    print(conv_num('0xAG4'))
    print(conv_num('x124'))
    print(conv_num('X124'))
