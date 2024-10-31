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

tipo_conv = input("Digite BD para converter de binário para decimal e DB para converter de decimal para binário.\n")
if tipo_conv.upper() == 'BD':
    tipo_conv = input("Digite I para converter um número inteiro e F para converter um número fracionário\n")
    if tipo_conv.upper() == 'I':
        bin = input("Digite o número em binário\n")
        decimal = binario_para_decimal(bin)
        print("O valor em decimal é igual a", decimal)
    elif tipo_conv.upper() == 'F':
        frac = input("Digite o número fracionário. Por favor, use vírgula como separador decimal.\n")
        partes = frac.split(",")
        pt_int = binario_para_decimal(partes[0])
        pt_fracionado = bin_frac_para_decimal(partes[1])

elif tipo_conv.upper() == 'DB':
    tipo_conv = input("Digite I para converter um número inteiro e F para converter um número fracionário\n")
    if tipo_conv.upper() == 'I':
        dec = int(input("Digite o número em decimal\n"))        
        print("O valor em binário é " + bin)
    elif tipo_conv.upper() == 'F':
        frac = input("Digite o número fracionário. Por favor, use vírgula como separador decimal.\n")
        partes = frac.split(",")
        pt_int = decimal_para_binario(partes[0])
        pt_fracionado = dec_frac_para_binario(partes[1])
        print(f'O número em binário é { pt_int }.{ pt_fracionado[2:] }')