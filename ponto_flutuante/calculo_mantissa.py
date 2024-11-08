def valor_minimo(beta, t, e):
    return 0.1 * (beta ** -e)

def valor_maximo(beta, t, e):
    val = "0." + (str(beta - 1) * t)
    return float(val) * (beta ** e)