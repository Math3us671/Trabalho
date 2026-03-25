import random

numero = int(input("Digite um Numero de 1 a 10:") )
sorteio = random.randint(1,10)



random.randint(1,10)

if numero == sorteio:
    print("Parabens seu beta acerto algo pelo menos", "O numero era", sorteio)
else:
    print("Beta moggado" )