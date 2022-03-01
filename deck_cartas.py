import random

# Classe para gerar as cartas, naipes, decks e valores de cada uma 
class DeckCartas():   
    
    naipe = ['Paus', 'Copas', 'Ouros', 'Espadas']
    cartas = ['As', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Valete', 'Dama', 'Rei']

    
    baralho = {}

    # Dois lacos de repeticao para gerar todas as 52 cartas     
    for index_naipe in naipe:
        for index_cartas in cartas:
            
            if index_cartas == 'As':
                i = 1
            if index_cartas == 'Valete' or index_cartas == 'Dama' or index_cartas == 'Rei':
                i = 10
            if index_cartas == '2' or index_cartas == '3' or index_cartas == '4' or index_cartas == '5' or index_cartas == '6' or index_cartas == '7' or index_cartas == '8' or index_cartas == '9' or index_cartas == '10':
                i = int(index_cartas)

            baralho[index_cartas + " de " + index_naipe] = i

    
    # Seleciona uma carta aleatoria do baralho e retorna a mesma
    def embaralhar():

        escolha_carta = random.choice(list(DeckCartas.baralho.keys()))
        return (escolha_carta, DeckCartas.baralho.pop(escolha_carta))
                  

