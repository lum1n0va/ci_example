def conv_num(num_str):
    """
    Takes a string in the form of decimal or hexadecimal
    Converts the strings to a base 10 number and returns it
    """
    sign_flag = False
    x_flag = False
    decimal_flag = False

    "Check to see if nothing was entered"
    if len(num_str) == 0:
        return None

    "Validate input prior to conversion"
    for char in range(0, len(num_str)):
        converted_char = ord(num_str[char])
        if char == 0 and converted_char == 45:  # Checks if the first char is a minus sign
            sign_flag = True
        elif converted_char == 46 and x_flag is False and decimal_flag is False:
            decimal_flag = True
        elif 48 <= converted_char <= 57:  # Checks if the char is a number
            pass
        elif 65 <= converted_char <= 70 or 97 <= converted_char <= 102 and x_flag is True:  # Checks if the char is an uppercase letter
            pass
        elif converted_char == 88 or converted_char == 120 and decimal_flag is False:
            if sign_flag is True and char == 2:
                x_flag = True
            elif char == 1:
                x_flag = True
            else:
                return None
        else:
            return None

    "Convert to the appropriate format"
    if x_flag is True:
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


if __name__ == '__main__':
    print(convert_decimal("394.6"))
    print(convert_decimal("32394.6"))
    print(convert_decimal("32394.64"))
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
