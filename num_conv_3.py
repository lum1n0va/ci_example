def conv_num(num_str):
    """
    Takes a string in the form of decimal or hexadecimal
    Converts the strings to a base 10 number and returns it
    """
    sign_flag = False
    zero_flag = False
    x_flag = False
    decimal_flag = False
    number_flag = False
    uppercase_flag = False
    lowercase_flag = False

    "Check to see if nothing was entered"
    if len(num_str) == 0:
        return None

    "Validate input prior to conversion"
    for char in range(0, len(num_str)):
        converted_char = ord(num_str[char])
        sign_flag = is_minus_sign(char, converted_char)
        if sign_flag is None:
            return None
        current_decimal_flag = is_decimal_point(converted_char, x_flag)
        if current_decimal_flag is None:
            return None
        number_flag = is_number(converted_char)
        uppercase_flag = is_uppercase_letter(converted_char)
        lowercase_flag = is_lowercase_letter(converted_char)
        current_x_flag = is_x(converted_char, decimal_flag)
        if current_x_flag is None:
            return None

        if decimal_flag is False and current_decimal_flag is True:
            decimal_flag = True
        elif x_flag is False and current_x_flag is True:
            if char == 1 and sign_flag is False:
                x_flag = True
            elif char == 2 and sign_flag is True:
                x_flag = True
        elif number_flag is False and uppercase_flag is False and lowercase_flag is False:
            return None


    "Convert to the appropriate format"
    if x_flag is True:
        converted_num = convert_hex(num_str)
    else:
        converted_num = convert_decimal(num_str)

    return converted_num


def is_minus_sign(char, converted_char):

    is_minus = False
    if char == 0 and converted_char == 45:
        is_minus = True
    elif converted_char == 45:
        is_minus = None
    return is_minus


def is_decimal_point(converted_char, x_flag):

    is_decimal = False
    if converted_char == 46 and x_flag is True:
        is_decimal = None
    elif converted_char == 46:
        is_decimal = True
    return is_decimal


def is_number(converted_char):

    is_digit = False
    if 48 <= converted_char <= 57:
        is_digit = True
    return is_digit


def is_uppercase_letter(converted_char):

    is_uppercase = False
    if 65 <= converted_char <= 70:
        is_uppercase = True
    return is_uppercase


def is_lowercase_letter(converted_char):

    is_lowercase = False
    if 97 <= converted_char <= 102:
        is_lowercase = True
    return is_lowercase


def is_x(converted_char, decimal_flag):

    is_x_flag = False
    if decimal_flag is True:
        is_x_flag = None
    elif converted_char == 88:
        is_x_flag = True
    elif converted_char == 120:
        is_x_flag = True
    return is_x_flag


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
