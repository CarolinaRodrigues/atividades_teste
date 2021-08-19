#CONJUNTO DE PASSOS            
#if -> estrutura simples
#if / else -> estrutura composta
#elif

#Exemplo 03
nota_1 = float(input('Digite a primiera nota: '))
nota_2 = float(input('Digite a segunda nota: '))
media = (nota_1 + nota_2)/2
print('A sua media foi {:.1f}'.format(media))
#condição simplificada
#print('PARABÉNS!' if media >= 6 else 'ESTUDE MAIS!')
if media >= 6.0:
    print('Sua media foi boa! PARABÉNS!')
else:
    print('Sua média foi ruim! ESTUDE MAIS!')










#######           EXEMPLOS     ###############
#tempo = int(input('Quanto tempo tem seus carro??'))
#if tempo <= 3:
#    print('carro novo')
#else:
#   print('carro velho')


#Exemplo 02

#nome = str(input('Qual é seu nome? '))
#if nome == 'Carolina':
#    print('Que nome lindo você tem!!')
#else:
#    print('Seu nome é tão normal!')
#print('Bom dia, {}!'.format(nome))
