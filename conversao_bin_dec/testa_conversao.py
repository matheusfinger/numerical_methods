import conversores

def teste():
    print(f'1010 em decimal é { conversores.binario_para_decimal("1010") }')
    print(f'1010,01 em decimal é { conversores.bin_frac_para_decimal("1010,01") }')
    print(f'12 em binário é { conversores.decimal_para_binario("12") }')
    print(f'12,25 em binário é { conversores.dec_frac_para_binario("12,25") }')

if __name__ == '__main__':
    teste()