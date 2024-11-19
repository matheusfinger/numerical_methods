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
