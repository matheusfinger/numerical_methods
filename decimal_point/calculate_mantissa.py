def min_val(beta: int, e: int):
    """
    Calculates the minimum value that can be represented by the machine
    """
    return 0.1 * (beta ** -e)

def max_val(beta: int, t: int, e: int):
    """
    Calculates the maximum value that can be represented by the machine
    """
    val = "0." + (str(beta - 1) * t)
    return float(val) * (beta ** e)

def num_max_mantissa_pos(beta: int, t: int):
    """
    Calculates the number of possible positive mantissas
    """
    return (beta - 1) * (beta ** (t - 1))

def num_max_exponent(u: int, l: int):
    """
    Calculates the number of possible exponents
    """
    return u - l + 1

def num_positive_elements(beta: int, t: int, u:int, l:int):
    """
    Calculates the number of representable positive elements
    """
    return num_max_mantissa_pos(beta, t) * num_max_exponent(u, l)

def total_representable_elements(beta: int, t: int, u:int, l:int):
    """
    Calculates the number of representable elements
    """
    return 2 * num_positive_elements(beta, t, u, l) + 1

def decimal_to_base(dec: int, beta: float):
    """
    Calculates the representation of a integer
    in a base.
    """
    bin = ""
    dec = int(dec)
    if dec == 0:
        return 0
    while dec != 0:
        bin += str(dec % beta)
        dec = dec // beta
    bin = bin[::-1]
    return bin

def dec_frac_to_base(dec: float, beta: int):
    """
    Calculates the representation of a float
    in a base
    """
    partes = dec.split(",")
    # Converting the integer part
    pt_int = decimal_to_base(partes[0], beta)
    decimal = partes[1]
    decimal = "0." + decimal
    decimal = float(decimal)
    bin = ""
    while decimal != 0:
        decimal = decimal * beta
        decimal = str(decimal)
        bin += decimal[0]
        if decimal[0] == '0':
            decimal = float(decimal)
        else:
            decimal =  float(decimal) - int(decimal[0])
    return pt_int + ',' + bin

def check_if_representable(number, beta, t, e):
    if number > max_val(beta, t, e):
        return "over"
    if number < min_val(beta, e):
        return "under"
    return "ok"

def normalize(number):
    parts = number.split(",")
    before = parts[0]
    after = parts[1]
    expoente = 0
    while len(before) > 1:
        expoente += 1
        after = before[-1] + after
        before = before[:len(before)-1]
    return (before + "," + after, expoente)

def truncar(number, limit):
    # limit should be the mantissa max length
    # if it is 2, then it will add 2 numbers
    return number[:limit+2]

def round_up(number, t):
    parts = number.split(",")
    parts[1] = parts[1][0:t]
    after = str(int(parts[1]) + 1)
    before = int(number[0])
    if len(after) > len(parts[1]):
        before += 1
        after = '0' * len(after) - 1
    return str(before) + "," + after

def arredondar(number, limit):
    if len(number) <= limit+2:
        return number
    if int(number[limit+2]) == 5:
        if len(number) >= 7 and int(number[limit+3:]) > 0:
            return round_up(number, limit)
        return number[:limit+2]
    if int(number[limit+2]) >= 5:
        return round_up(number, limit)
    return number[:limit+2]


def convert_final(metodo, number, beta, t, e):
    # Convertendo para float
    test_number = number.replace(',', '.')
    test_number = float(test_number)
    test = check_if_representable(test_number, beta, t, e)
    if test == 'ok':
        result = dec_frac_to_base(number, beta)
        result, expoente = normalize(result)
        if metodo == 'arredondamento':
            result = arredondar(result, t)
        else:
            result = truncar(result, t)
        return (result, expoente)
    if test == 'over':
        return "Overflow error"
    return "Underflow error"