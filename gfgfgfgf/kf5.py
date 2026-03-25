import random

robo = random.randint (1,10)

parouimpar = str(input("Escolha par ou impar: ") )

numero = int(input("Digite um  número de 1 a 10: ") )

soma = robo + numero

print("Você escolheu", numero)
print("Computador:", robo)
print("Total:", soma)

if soma%2 == 0:
    print('RAHHHHHH')
    resultado = 'par'
else:
    print('IMRAHHHH')
    resultado = 'impar'
if parouimpar == resultado:
    print('Jogador ganhou!')
else:
    print("Computador ganhou!")















