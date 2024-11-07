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
    partes = bin.split(",")
    pt_int = binario_para_decimal(partes[0])
    binario = partes[1]
    dec = 0
    cont = -1
    for digito in binario:
        dec += int(digito) * (2 ** cont)
        cont -= 1
    return pt_int + ',' + str(dec)[2:]

def decimal_para_binario(dec):
    bin = ""
    dec = int(dec)
    if dec == 0:
        return 0
    while dec != 0:
        bin += str(dec % 2)
        dec = dec // 2
    bin = bin[::-1]
    return bin

def dec_frac_para_binario(dec):
    partes = dec.split(",")
    pt_int = decimal_para_binario(partes[0])
    decimal = partes[1]
    decimal = "0." + decimal
    decimal = float(decimal)
    bin = ""
    while decimal != 0:
        decimal = decimal * 2
        decimal = str(decimal)
        bin += decimal[0]
        if decimal[0] == '0':
            decimal = float(decimal)
        else:
            decimal =  float(decimal) - int(decimal[0])
    return pt_int + ',' + bin