import calculate_mantissa
print("Usando arredondamento")
numero, expoente = calculate_mantissa.convert_final("arredondamento", "13,123", 10, 6, 4)
print(f'O número 13,123 na base 10, t de 6, expoente de -4 a 4 é:\n {numero} x 10^{expoente}')
