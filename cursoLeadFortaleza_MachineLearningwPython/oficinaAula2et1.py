#etapa 1
import random
listaJogadas = ['', 'Pedra', 'Papel', 'Tesoura', 'Sair']
while True:
    suaJogada = int(input("Escolha uma opção (1, 2, 3 ou 4):\n1 - Pedra\n2 - Papel\n3 - Tesoura\n4 - Sair\n: "))
    print("Sua jogada -> " + listaJogadas[suaJogada])
    if suaJogada == 4:
        print('Saindo...')
        break
    maqJogada = random.choice(["Pedra", "Papel", "Tesoura"])
    print("Jogada da máquina -> " + maqJogada)
    if maqJogada == listaJogadas[suaJogada]:
        print("Empate!")
    else:
        if maqJogada == 'Pedra':
            if listaJogadas[suaJogada] == 'Tesoura':
                print("Você ganhou!")
            else:
                print("Você perdeu!")
        elif maqJogada == 'Papel':
            if listaJogadas[suaJogada] == 'Pedra':
                print("Você ganhou!")
            else:
                print("Você perdeu!")
        elif maqJogada == 'Tesoura':
            if listaJogadas[suaJogada] == 'Papel':
                print("Você ganhou!")
            else:
                print("Você perdeu!")

###################################################################
#etapa 2
import random
import math
listaJogadas = ['', 'Pedra', 'Papel', 'Tesoura', 'Sair']
jogados = []
pesos = [1, 1, 1]
def zeroR(jogados):
    for i in range(len(jogados)):
        if jogados[i] == 'Pedra':
            pesos[0] = pesos[0] + 1
        elif jogados[i] == 'Papel':
            pesos[1] = pesos[1] + 1
        elif jogados[i] == 'Tesoura':
            pesos[2] = pesos[2] + 1
    return pesos
while True:
    suaJogada = int(input("Escolha uma opção (1, 2, 3 ou 4):\n1 - Pedra\n2 - Papel\n3 - Tesoura\n4 - Sair\n: "))
    print("Sua jogada -> " + listaJogadas[suaJogada])
    jogados.append(listaJogadas[suaJogada]) 
    if suaJogada == 4:
        print('Saindo...')
        break
    if len(jogados) < 5:
        maqJogada = random.choice(["Pedra", "Papel", "Tesoura"])
    else:
        pesos = zeroR(jogados)
        maqJogada = random.choices(["Pedra", "Papel", "Tesoura"], weights = pesos, k=1)[0]
    print("Jogada da máquina -> " + maqJogada)
    if maqJogada == listaJogadas[suaJogada]:
        print("Empate!")
    else:
        if maqJogada == 'Pedra':
            if listaJogadas[suaJogada] == 'Tesoura':
                print("Você ganhou!")
            else:
                print("Você perdeu!")
        elif maqJogada == 'Papel':
            if listaJogadas[suaJogada] == 'Pedra':
                print("Você ganhou!")
            else:
                print("Você perdeu!")
        elif maqJogada == 'Tesoura':
            if listaJogadas[suaJogada] == 'Papel':
                print("Você ganhou!")
            else:
                print("Você perdeu!")
