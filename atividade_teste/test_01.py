

def base_16_numero_letra(letra):
    numero = 0
    
    return{
    
        'A':10,
        'B':11,
        'C':12,
        'D':13,
        'E':14,
        'F':15,
        'numero': letra
    }.get(letra)

letra = ('b')
#letra = str(input('informe uma letra: '))
base_16_numero_letra(letra.upper())
print(base_16_numero_letra(letra.upper()))