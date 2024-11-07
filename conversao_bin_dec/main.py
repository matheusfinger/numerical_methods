import conversores

def teste():
    tipo_conv = input("Digite BD para converter de binário para decimal e DB para converter de decimal para binário.\n")
    if tipo_conv.upper() == 'BD':
        tipo_conv = input("Digite I para converter um número inteiro e F para converter um número fracionário\n")
        if tipo_conv.upper() == 'I':
            bin = input("Digite o número em binário\n")
            dec = conversores.binario_para_decimal(bin)
        elif tipo_conv.upper() == 'F':
            frac = input("Digite o número fracionário. Por favor, use vírgula como separador decimal.\n")
            dec = conversores.bin_frac_para_decimal(frac)
        print(f'O número em decimal é { dec }')

    elif tipo_conv.upper() == 'DB':
        tipo_conv = input("Digite I para converter um número inteiro e F para converter um número fracionário\n")
        if tipo_conv.upper() == 'I':
            dec = int(input("Digite o número em decimal\n"))        
            bin = conversores.decimal_para_binario(dec)
        elif tipo_conv.upper() == 'F':
            frac = input("Digite o número fracionário. Por favor, use vírgula como separador decimal.\n")
            bin = conversores.dec_frac_para_binario(frac)
        print(f'O número em binário é { bin }')

if __name__ == '__main__':
    teste()