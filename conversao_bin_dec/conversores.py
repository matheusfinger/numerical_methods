def binario_para_decimal(bin):
    soma = 0
    exp = 0
    for i in range(len(bin)-1, -1, -1):
        if bin[i] != '0' and bin[i] != '1':
            raise Exception("O valor não está em binário (0 e 1)")
        soma = soma + (int(bin[i]) * (2 ** exp))
        exp += 1
    return str(soma)

def bin_frac_para_decimal(bin):
    return bin

def decimal_para_binario(dec):
    bin = ""
    dec = int(dec)
    if dec == 0:
        return 0
    while dec != 0:
        print(dec)
        bin += str(dec % 2)
        dec = dec // 2
    bin = bin[::-1]
    return bin

def dec_frac_para_binario(dec):
    dec = "0." + dec
    dec = float(dec)
    bin = "0."
    while dec != 0:
        print(dec)
        print()
        dec = dec * 2
        dec = str(dec)
        bin += dec[0]
        if dec[0] == '0':
            dec = float(dec)
        else:
            dec =  float(dec) - int(dec[0])
    return bin