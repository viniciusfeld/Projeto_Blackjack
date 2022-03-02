from deck_cartas import DeckCartas
import random
import time
import os

#Funcao main aonde ira chamar todas as funcoes e metodos
def main():
    #Recebe o retorno da funcao menu para saber em qual metodo entrar
    opcao = menu()
    #Tratativa para proibir entrada de valores diferentes de 1 ou 2    
    if opcao == '1':
        jogoCPU()
    elif opcao == '2':
        jogoDois()
    elif opcao != '1' or opcao != '2':
        print("Por gentileza, digitar um valor correspondente a 1 ou 2")
        time.sleep(2)
        main()    
    #Validacao se o jogador gostaria de jogar novamente
    print("\nGostaria de jogar novamente?(y/n)")
    comando = input()
    if comando == 'n':
        print("\n\nObrigado e espero que tenha gostado :)")
    else:
        main()


#Funcao para mostrar o menu de opcoes e regras
def menu():
    print("""
    Seja bem vindo ao BlackJack em Python:

    ====================================================================
    --- Antes de começarmos, vamos para as regras ---
    - A carta Ás irá valer sempre 1 -
    - A cada final de uma rodada, será embaralhado as cartas - 
    - Se divirta -
    ====================================================================
                
                1 - Jogar contra CPU
                2 - Jogar contra outro jogador
    """)

    comando = input()

    return comando

# Funcao para jogar contra o CPU
def jogoCPU():
    #Limpador de tela
    os.system('clear') or None
    print("Antes de começarmos o jogo, digite seu nick, por favor: ")
    nome_jogador = input()
    print(f"Ok {nome_jogador}, vamos começar!!!")
    cartas_jogador = []
    cartas_cpu = []
    cartas_iniciais = 0
    visual_carta = """
                     ___
                    |   |
                    |___|                
                    
                    """
    # Laco correspondente as 2 primeiras cartas do começo do jogo
    while cartas_iniciais != 2:
        # Chama a classe e a funcao para pegar uma carta aleatoria do deck
        i = DeckCartas.embaralhar()
        #Insere a carta em uma lista
        cartas_jogador.append(i)
        cartas_iniciais += 1 

    # Soma dos valores das cartas sortiadas
    soma_cartas_jogador = cartas_jogador[0][1] + cartas_jogador[1][1]
    print(f"""Suas cartas são:{visual_carta}{cartas_jogador[0]}{visual_carta}{cartas_jogador[1]}                                    
                    
Soma = {soma_cartas_jogador}
                    """)
    print("Gostaria de mais uma carta(y/n)? " )
    comando = input()
    os.system('clear') or None

    while comando == 'y':
        # Verifica se o jogador estourou
        if soma_cartas_jogador >= 21:
            break    
        if comando == 'y':
            i = DeckCartas.embaralhar()
            cartas_jogador.append(i)
            soma_cartas_jogador += cartas_jogador[2][1]

            print(f"""Suas cartas são:{visual_carta}{cartas_jogador[0]}{visual_carta}{cartas_jogador[1]}{visual_carta}{cartas_jogador[2]}

Soma = {soma_cartas_jogador}     
                                """)
            
            # Caso o jogador estoure, ele finaliza a vez e sai do laço
            if soma_cartas_jogador >= 21:
                print("Vez do CPU....")
                time.sleep(1)
                break                

            print("Gostaria de mais uma carta(y/n)? ")            
            comando = input()    
                
            os.system('clear') or None

            if comando == 'y':

                i = DeckCartas.embaralhar()
                cartas_jogador.append(i)
                soma_cartas_jogador += cartas_jogador[3][1]

                print(f"""Suas cartas são:{visual_carta}{cartas_jogador[0]}{visual_carta}{cartas_jogador[1]}{visual_carta}{cartas_jogador[2]}{visual_carta}{cartas_jogador[3]}

Soma = {soma_cartas_jogador}     
                                    """)
                
                if soma_cartas_jogador >= 21:
                    print("Vez do CPU....")
                    time.sleep(1)
                    break

                print("Gostaria de mais uma carta(y/n)? " )

                comando = input()

                os.system('clear') or None
            cont = 4
            while comando == 'y':
                i = DeckCartas.embaralhar()
                cartas_jogador.append(i)
                soma_cartas_jogador += cartas_jogador[cont][1]        

                print(f"""Vamos poupar processamento a partir de agora :)

                    Suas cartas são:
                    {cartas_jogador}
Soma = {soma_cartas_jogador} 
                """)
                if soma_cartas_jogador >= 21:
                    print("Vez do CPU....")
                    time.sleep(1)
                    break

                print("Gostaria de mais uma carta(y/n)? " )
                comando = input()

                os.system('clear') or None
                cont = cont + 1
    
    print("Seu adversário esta recebendo as cartas...")
    time.sleep(3)
    
    # Laço para gerar as 2 primeiras cartas do CPU
    cartas_iniciais = 0
    while cartas_iniciais != 2:
        i = DeckCartas.embaralhar()
        cartas_cpu.append(i)
        cartas_iniciais += 1

    soma_cartas_cpu = cartas_cpu[0][1] + cartas_cpu[1][1]

    # Laço para ficar pedindo carta enquanto a soma for menor ou igual a 18
    while soma_cartas_cpu <=18:
        i = DeckCartas.embaralhar()
        cartas_cpu.append(i)
        soma_cartas_cpu += cartas_cpu[cartas_iniciais][1]
        cartas_iniciais += 1

    # Verifica empate
    if soma_cartas_jogador == soma_cartas_cpu:
        print(f"As cartas do {nome_jogador}:", cartas_jogador)
        print(f"\nSoma das cartas do {nome_jogador}:", soma_cartas_jogador)
        print("\n\nAs cartas do CPU:", cartas_cpu)
        print("\nSoma das cartas do CPU:", soma_cartas_cpu)
        print("\nEmpate entre os Jogadores :)")

        return 1

    # Verifica se o jogador fechou 21
    if soma_cartas_jogador == 21:
        print(f"As cartas do {nome_jogador}:", cartas_jogador)
        print(f"\nSoma das cartas do {nome_jogador}:", soma_cartas_jogador)
        print("\n\nAs cartas do CPU:", cartas_cpu)
        print("\nSoma das cartas do CPU:", soma_cartas_cpu)
        print(f"\n\nVitoria do {nome_jogador} :)")

        return 1

    # Verifica se o CPU fechou 21  
    if soma_cartas_cpu == 21:
        print(f"As cartas do {nome_jogador}:", cartas_jogador)
        print(f"\nSoma das cartas do {nome_jogador}:", soma_cartas_jogador)
        print("\n\nAs cartas do CPU:", cartas_cpu)
        print("\nSoma das cartas do CPU:", soma_cartas_cpu)
        print("\n\nVitoria do CPU :)")

        return 1
    
    #Verifica se os 2 jogadores estouraram, e qual dois dois estourou mais
    if soma_cartas_cpu > 21 and soma_cartas_jogador > 21:
        if soma_cartas_cpu < soma_cartas_jogador:
            print(f"As cartas do {nome_jogador}:", cartas_jogador)
            print(f"\nSoma das cartas do {nome_jogador}:", soma_cartas_jogador)
            print("\n\nAs cartas do CPU:", cartas_cpu)
            print("\nSoma das cartas do CPU:", soma_cartas_cpu)
            print("\nAmbos estouraram, porem o CPU estourou menos")
            print("\n\nVitoria do CPU :)")
            return 1
        else:
            print(f"As cartas do {nome_jogador}:", cartas_jogador)
            print(f"\nSoma das cartas do {nome_jogador}:", soma_cartas_jogador)
            print("\n\nAs cartas do CPU:", cartas_cpu)
            print("\nSoma das cartas do CPU:", soma_cartas_cpu)
            print(f"\nAmbos estouraram, porem o {nome_jogador} estourou menos")
            print(f"\n\nVitoria do {nome_jogador} :)")
            return 1

    #Verifica se ambos tiraram 21 ou menos
    if soma_cartas_cpu <= 21 and soma_cartas_jogador <= 21:
        #Verfica quem tirou mais entre os 2
        if soma_cartas_cpu > soma_cartas_jogador:
            print(f"As cartas do {nome_jogador}:", cartas_jogador)
            print(f"\nSoma das cartas do {nome_jogador}:", soma_cartas_jogador)
            print("\n\nAs cartas do CPU:", cartas_cpu)
            print("\nSoma das cartas do CPU:", soma_cartas_cpu)
            print("\n\nVitoria do CPU :)")
            return 1

        elif soma_cartas_jogador > soma_cartas_cpu:
            print(f"As cartas do {nome_jogador}:", cartas_jogador)
            print(f"\nSoma das cartas do {nome_jogador}:", soma_cartas_jogador)
            print("\n\nAs cartas do CPU:", cartas_cpu)
            print("\nSoma das cartas do CPU:", soma_cartas_cpu)
            print(f"\n\nVitoria do {nome_jogador} :)")
            return 1
    
    # Verifica se o CPU tirou menos que o jogador e menos ou igual a 21
    if soma_cartas_cpu < soma_cartas_jogador and soma_cartas_cpu <=21:
        print(f"As cartas do {nome_jogador}:", cartas_jogador)
        print(f"\nSoma das cartas do {nome_jogador}:", soma_cartas_jogador)
        print("\n\nAs cartas do CPU:", cartas_cpu)
        print("\nSoma das cartas do CPU:", soma_cartas_cpu)
        print("\n\nVitoria do CPU :)")
        return 1

    # Verifica se o jogador tirou menos que o cpu e menos ou igual a 21
    if soma_cartas_jogador < soma_cartas_cpu and soma_cartas_jogador <=21:
        print(f"As cartas do {nome_jogador}:", cartas_jogador)
        print(f"\nSoma das cartas do {nome_jogador}:", soma_cartas_jogador)
        print("\n\nAs cartas do CPU:", cartas_cpu)
        print("\nSoma das cartas do CPU:", soma_cartas_cpu)
        print(f"\n\nVitoria do {nome_jogador} :)")
        return 1


# Funcao para jogar blackjack em 2 players
def jogoDois():
    os.system('clear') or None
    #Coleta os nicks de cada jogador
    print("Antes de começarmos o jogo, digite o nick do primeiro jogador, por favor: ")
    nome_jogador1 = input()
    print("Agora digite o nome do segundo jogador, por favor: ")
    nome_jogador2 = input()
    print(f"Ok {nome_jogador1} e {nome_jogador2}, vamos começar!!!")
    time.sleep(2)
    os.system('clear') or None
    print(f"Vamos começar com o {nome_jogador1}")
    time.sleep(1)
    cartas_jogador1 = []
    cartas_jogador2 = []
    cartas_iniciais = 0
    visual_carta = """
                     ___
                    |   |
                    |___|                
                    
                """
    # Laco para gerar as 2 primeiras cartas do primeiro jogador
    while cartas_iniciais != 2:
        i = DeckCartas.embaralhar()
        cartas_jogador1.append(i)
        cartas_iniciais += 1    

    # Soma dos valores das cartas
    soma_cartas_jogador1 = cartas_jogador1[0][1] + cartas_jogador1[1][1]
    print(f"Jogando {nome_jogador1}")
    print(f"""Suas cartas são:{visual_carta}{cartas_jogador1[0]}{visual_carta}{cartas_jogador1[1]}                                    
                    
Soma = {soma_cartas_jogador1}
                    """)
    print("Gostaria de mais uma carta(y/n)? " )
    comando = input()
    os.system('clear') or None

    while comando == 'y':
        #Verifica se o jogador 1 estourou
        if soma_cartas_jogador1 >= 21:
            break    
        if comando == 'y':
            i = DeckCartas.embaralhar()
            cartas_jogador1.append(i)
            soma_cartas_jogador1 += cartas_jogador1[2][1]
            print(f"Jogando {nome_jogador1}")
            print(f"""Suas cartas são:{visual_carta}{cartas_jogador1[0]}{visual_carta}{cartas_jogador1[1]}{visual_carta}{cartas_jogador1[2]}

Soma = {soma_cartas_jogador1}     
                                """)
            
            #Verifica se o jogador 1 estourou e vai para a vez do jogador 2
            if soma_cartas_jogador1 >= 21:
                print(f"Vez do {nome_jogador2}....")
                time.sleep(1)
                print("A tela sera limpa...")
                time.sleep(2)
                os.system('clear') or None
                break                

            print("Gostaria de mais uma carta(y/n)? " )
            comando = input()    
            
            os.system('clear') or None

            if comando == 'y':

                i = DeckCartas.embaralhar()
                cartas_jogador1.append(i)
                soma_cartas_jogador1 += cartas_jogador1[3][1]
                print(f"Jogando {nome_jogador1}")
                print(f"""Suas cartas são:{visual_carta}{cartas_jogador1[0]}{visual_carta}{cartas_jogador1[1]}{visual_carta}{cartas_jogador1[2]}{visual_carta}{cartas_jogador1[3]}

Soma = {soma_cartas_jogador1}     
                                    """)
                
                if soma_cartas_jogador1 >= 21:
                    print(f"Vez do {nome_jogador2}....")
                    time.sleep(1)
                    print("A tela sera limpa...")
                    time.sleep(2)
                    os.system('clear') or None
                    break

                print("Gostaria de mais uma carta(y/n)? " )
                comando = input()

                os.system('clear') or None

            # Laco para evitar repeticao de codigo
            cont = 4
            while comando == 'y':
                i = DeckCartas.embaralhar()
                cartas_jogador1.append(i)
                soma_cartas_jogador1 += cartas_jogador1[cont][1]        
                print(f"Jogando {nome_jogador1}")
                print(f"""Vamos poupar processamento a partir de agora :)

                    Suas cartas são:
                    {cartas_jogador1}
Soma = {soma_cartas_jogador1} 
                """)
                if soma_cartas_jogador1 >= 21:
                    print(f"Vez do {nome_jogador2}....")
                    time.sleep(1)
                    print("A tela sera limpa...")
                    time.sleep(2)
                    os.system('clear') or None
                    break

                print("Gostaria de mais uma carta(y/n)? " )
                comando = input()

                os.system('clear') or None
                cont = cont + 1
    
    #Passando a vez para o jogador 2
    print(f"Passando a vez para o jogador {nome_jogador2}")
    time.sleep(2)
    cartas_iniciais = 0
    while cartas_iniciais != 2:
        i = DeckCartas.embaralhar()
        cartas_jogador2.append(i)
        cartas_iniciais += 1    

    soma_cartas_jogador2 = cartas_jogador2[0][1] + cartas_jogador2[1][1]
    print(f"Jogando {nome_jogador2}")
    print(f"""Suas cartas são:{visual_carta}{cartas_jogador2[0]}{visual_carta}{cartas_jogador2[1]}                                    
                    
Soma = {soma_cartas_jogador2}
                    """)
    print("Gostaria de mais uma carta(y/n)? " )
    comando = input()
    os.system('clear') or None

    while comando == 'y':
        if soma_cartas_jogador2 >= 21:
            break    
        if comando == 'y':
            i = DeckCartas.embaralhar()
            cartas_jogador2.append(i)
            soma_cartas_jogador2 += cartas_jogador2[2][1]
            print(f"Jogando {nome_jogador2}")
            print(f"""Suas cartas são:{visual_carta}{cartas_jogador2[0]}{visual_carta}{cartas_jogador2[1]}{visual_carta}{cartas_jogador2[2]}

Soma = {soma_cartas_jogador2}     
                                """)
            
            #Verifica se estourou e finaliza o jogo, caso seja True
            if soma_cartas_jogador2 >= 21:
                print("Calculando Resultado...")
                time.sleep(2)
                os.system('clear') or None
                break                

            print("Gostaria de mais uma carta(y/n)? " )
            comando = input()    
            
            os.system('clear') or None

            if comando == 'y':

                i = DeckCartas.embaralhar()
                cartas_jogador2.append(i)
                soma_cartas_jogador2 += cartas_jogador2[3][1]                
                print(f"Jogando {nome_jogador2}")
                print(f"""Suas cartas são:{visual_carta}{cartas_jogador2[0]}{visual_carta}{cartas_jogador2[1]}{visual_carta}{cartas_jogador2[2]}{visual_carta}{cartas_jogador2[3]}

Soma = {soma_cartas_jogador2}     
                                    """)
                
                if soma_cartas_jogador2 >= 21:
                    print("Calculando Resultado...")
                    time.sleep(2)
                    os.system('clear') or None
                    break

                print("Gostaria de mais uma carta(y/n)? " )
                comando = input()

                os.system('clear') or None

            cont = 4
            while comando == 'y':
                i = DeckCartas.embaralhar()
                cartas_jogador2.append(i)
                soma_cartas_jogador2 += cartas_jogador2[cont][1]        

                print(f"Jogando {nome_jogador2}")
                print(f"""Vamos poupar processamento a partir de agora :)

                    Suas cartas são:
                    {cartas_jogador2}
Soma = {soma_cartas_jogador2} 
                """)
                if soma_cartas_jogador2 >= 21:
                    print("Calculando Resultado...")
                    time.sleep(2)
                    os.system('clear') or None
                    break

                print("Gostaria de mais uma carta(y/n)? " )
                comando = input()

                os.system('clear') or None
                cont = cont + 1

    print("Calculando Resultados...")
    time.sleep(2)

    # Verifica se os jogadores empataram
    if soma_cartas_jogador1 == soma_cartas_jogador2:
        print(f"As cartas do {nome_jogador1}:", cartas_jogador1)
        print(f"\nSoma das cartas do {nome_jogador1}:", soma_cartas_jogador1)
        print(f"\n\nAs cartas do {nome_jogador2}:", cartas_jogador2)
        print(f"\nSoma das cartas do {nome_jogador2}:", soma_cartas_jogador2)
        print("\nEmpate entre os Jogadores :)")

        return 1

    if soma_cartas_jogador1 == 21:
        print(f"As cartas do {nome_jogador1}:", cartas_jogador1)
        print(f"\nSoma das cartas do {nome_jogador1}:", soma_cartas_jogador1)
        print(f"\n\nAs cartas do {nome_jogador2}:", cartas_jogador2)
        print(f"\nSoma das cartas do {nome_jogador2}:", soma_cartas_jogador2)
        print(f"\n\nVitoria do {nome_jogador1} :)")

        return 1
    
    if soma_cartas_jogador2 == 21:
        print(f"As cartas do {nome_jogador1}:", cartas_jogador1)
        print(f"\nSoma das cartas do {nome_jogador1}:", soma_cartas_jogador1)
        print(f"\n\nAs cartas do {nome_jogador2}:", cartas_jogador2)
        print(f"\nSoma das cartas do {nome_jogador2}:", soma_cartas_jogador2)
        print(f"\n\nVitoria do {nome_jogador2} :)")

        return 1

    #Verifica se um jogador estourou e o outro nao
    if soma_cartas_jogador1 > 21 and soma_cartas_jogador2 < 21:
        print(f"As cartas do {nome_jogador1}:", cartas_jogador1)
        print(f"\nSoma das cartas do {nome_jogador1}:", soma_cartas_jogador1)
        print(f"\n\nAs cartas do {nome_jogador2}:", cartas_jogador2)
        print(f"\nSoma das cartas do {nome_jogador2}:", soma_cartas_jogador2)
        print(f"\n\nVitoria do {nome_jogador2} :)")

        return 1

    if soma_cartas_jogador1 < 21 and soma_cartas_jogador2 > 21:
        print(f"As cartas do {nome_jogador1}:", cartas_jogador1)
        print(f"\nSoma das cartas do {nome_jogador1}:", soma_cartas_jogador1)
        print(f"\n\nAs cartas do {nome_jogador2}:", cartas_jogador2)
        print(f"\nSoma das cartas do {nome_jogador2}:", soma_cartas_jogador2)
        print(f"\n\nVitoria do {nome_jogador1} :)")

        return 1

    if soma_cartas_jogador2 > 21 and soma_cartas_jogador1 > 21:
        if soma_cartas_jogador2 < soma_cartas_jogador1:
            print(f"As cartas do {nome_jogador1}:", cartas_jogador1)
            print(f"\nSoma das cartas do {nome_jogador1}:", soma_cartas_jogador1)
            print(f"\n\nAs cartas do {nome_jogador2}:", cartas_jogador2)
            print(f"\nSoma das cartas do {nome_jogador2}:", soma_cartas_jogador2)
            print(f"\nAmbos os jogadores estouraram, porem o {nome_jogador2} estourou menos")
            print(f"\n\nVitoria do {nome_jogador2} :)")

            return 1
        else:
            print(f"As cartas do {nome_jogador1}:", cartas_jogador1)
            print(f"\nSoma das cartas do {nome_jogador1}:", soma_cartas_jogador1)
            print(f"\n\nAs cartas do {nome_jogador2}:", cartas_jogador2)
            print(f"\nSoma das cartas do {nome_jogador2}:", soma_cartas_jogador2)
            print(f"\nAmbos os jogadores estouraram, porem o {nome_jogador1} estourou menos")
            print(f"\n\nVitoria do {nome_jogador1} :)")

            return 1

    if soma_cartas_jogador1 <= 21 and soma_cartas_jogador2 <= 21:
        if soma_cartas_jogador1 > soma_cartas_jogador2:
            print(f"As cartas do {nome_jogador1}:", cartas_jogador1)
            print(f"\nSoma das cartas do {nome_jogador1}:", soma_cartas_jogador1)
            print(f"\n\nAs cartas do {nome_jogador2}:", cartas_jogador2)
            print(f"\nSoma das cartas do {nome_jogador2}:", soma_cartas_jogador2)
            print(f"\n\nVitoria do {nome_jogador1} :)")

            return 1

        elif soma_cartas_jogador2 > soma_cartas_jogador1:
            print(f"As cartas do {nome_jogador1}:", cartas_jogador1)
            print(f"\nSoma das cartas do {nome_jogador1}:", soma_cartas_jogador1)
            print(f"\n\nAs cartas do {nome_jogador2}:", cartas_jogador2)
            print(f"\nSoma das cartas do {nome_jogador2}:", soma_cartas_jogador2)
            print(f"\n\nVitoria do {nome_jogador2} :)")

            return 1
    
    if soma_cartas_jogador1 < soma_cartas_jogador2 and soma_cartas_jogador1 <=21:
        print(f"As cartas do {nome_jogador1}:", cartas_jogador1)
        print(f"\nSoma das cartas do {nome_jogador1}:", soma_cartas_jogador1)
        print(f"\n\nAs cartas do {nome_jogador2}:", cartas_jogador2)
        print(f"\nSoma das cartas do {nome_jogador2}:", soma_cartas_jogador2)
        print(f"\n\nVitoria do {nome_jogador1} :)")

        return 1

    if soma_cartas_jogador2 < soma_cartas_jogador1 and soma_cartas_jogador2 <=21:
        print(f"As cartas do {nome_jogador1}:", cartas_jogador1)
        print(f"\nSoma das cartas do {nome_jogador1}:", soma_cartas_jogador1)
        print(f"\n\nAs cartas do {nome_jogador2}:", cartas_jogador2)
        print(f"\nSoma das cartas do {nome_jogador2}:", soma_cartas_jogador2)
        print(f"\n\nVitoria do {nome_jogador1} :)")

        return 1 
 
main()