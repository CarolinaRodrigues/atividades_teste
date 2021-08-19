#Conversão de Bases

#CONVERSÃO DE BASE 2 PARA BASE 10 
def base_2_para_base_10(valor_para_converter): 
  tamanho_valor = len(valor_para_converter)
  valor_convertido = 0
  i = 0 
  while tamanho_valor > 0:
    
    numero_posicao_atual = valor_para_converter[tamanho_valor - 1]
    
    tamanho_valor = tamanho_valor - 1
    
    if(numero_posicao_atual == '1'): 
      valor_convertido = valor_convertido + ((int(numero_posicao_atual) * 2) ** int(i))
    
    i = i + 1
  return valor_convertido

#CONVERSÃO DE BASE 2 PARA BASE 16
def base_2_para_base_16(valor_para_converter,base_origem):
    
    base_10 = base_2_para_base_10(valor_para_converter)
    return base_10_para_base_x(base_10,16)





#CONVERSÃO BASE 10  PARA BASE X
def base_10_para_base_x(valor_para_converter,base):
    valor_para_converter = int(valor_para_converter)
    base = int(base)
    digits = "0123456789ABCDEF"

    remstack = []

    while valor_para_converter > 0:
        rem = valor_para_converter % base
        remstack.append(rem)
        valor_para_converter = valor_para_converter // base

    base_x = ""

    for r in remstack[::-1]:
        
        base_x = base_x + digits[r]
    print(base_x)
    return base_x



#CONVERSÃO BASE 16
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

#CONVERSÃO DA BASE 16 PARA BASE 10
def base_16_para_base_10(valor_para_converter): 
  tamanho_valor = len(valor_para_converter)
  numero_posicao_atual = 0
  while tamanho_valor > 0:
    
    numero_posicao_atual = numero_posicao_atual + int(base_16_numero_letra(valor_para_converter.upper()[tamanho_valor - 1]))
    
    tamanho_valor = tamanho_valor - 1

  return numero_posicao_atual

def base_16_para_base_2(valor_para_converter): 
    base_10 = base_16_para_base_10(valor_para_converter)
    return base_10_para_base_x(base_10,2)



# BASE X
def base_2_para_base_x(valor_para_converter,base_destino):
    

    if(base_destino == '10'):
       base_10 = base_2_para_base_10(valor_para_converter)
       return base_10
    
    if(base_destino == '16'):
       base_10 = base_2_para_base_10(valor_para_converter)
       print(base_10)
       return base_10_para_base_x(base_10,16)
    if(base_destino == '2'):
       print("Não é possivel converter base origem igual base destino")

#CONVERSÃO DA BASE 16 PARA BASE X
def base_16_para_base_x(valor_para_converter,base_destino):
    if(base_destino == '2'): 
      return base_16_para_base_2(valor_para_converter)
    if(base_destino == '10'): 
        return base_16_para_base_10(valor_para_converter)

#VALORES DE ENTRADA 
def valores_de_entrada(valor_para_converter,base_origem,base_destino):
    
    if base_origem == '2':
        return base_2_para_base_x(valor_para_converter,base_destino)
    if  base_origem == '10':
        return base_10_para_base_x(valor_para_converter,base_destino)
    if  base_origem == '16':
        return base_16_para_base_x(valor_para_converter,base_destino)

valor = valores_de_entrada('1010','2','16')
print(str(valor))