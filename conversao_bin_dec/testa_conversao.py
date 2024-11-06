import conversores

def teste():
    tipo_conv = input("Digite BD para converter de binário para decimal e DB para converter de decimal para binário.\n")
    if tipo_conv.upper() == 'BD':
        tipo_conv = input("Digite I para converter um número inteiro e F para converter um número fracionário\n")
        if tipo_conv.upper() == 'I':
            bin = input("Digite o número em binário\n")
            decimal = conversores.binario_para_decimal(bin)
            print("O valor em decimal é igual a", decimal)
        elif tipo_conv.upper() == 'F':
            frac = input("Digite o número fracionário. Por favor, use vírgula como separador decimal.\n")
            partes = frac.split(",")
            pt_int = conversores.binario_para_decimal(partes[0])
            pt_fracionado = conversores.bin_frac_para_decimal(partes[1])

    elif tipo_conv.upper() == 'DB':
        tipo_conv = input("Digite I para converter um número inteiro e F para converter um número fracionário\n")
        if tipo_conv.upper() == 'I':
            dec = int(input("Digite o número em decimal\n"))        
            print("O valor em binário é " + bin)
        elif tipo_conv.upper() == 'F':
            frac = input("Digite o número fracionário. Por favor, use vírgula como separador decimal.\n")
            partes = frac.split(",")
            pt_int = conversores.decimal_para_binario(partes[0])
            pt_fracionado = conversores.dec_frac_para_binario(partes[1])
            print(f'O número em binário é { pt_int }.{ pt_fracionado[2:] }')

if __name__ == '__main__':
    teste()