from random import shuffle as suf
from datetime import datetime
from .models import MajorArcana

#faire Connaiscance
inputs = []
def clairvoyant(input_value):    
    msg = [
        {"messages" : "Muito obrigada " + input_value.capitalize() + " !" +
        " Vou baralhando as cartas..." +
        " Agora a sua data de nascimento (en formato 'AAAA-MM-DD') ! "},
        {"messages" : "Obrigada !" +
        " Mais duas persuntas.. Estamos quase a saber o que o destino nos diz!" +
        " Afins de cortar o baralho em dois, preciso de um numero (de 1 a 38 incluidos)!"},
        {"messages" : "Por ultimo, tenho aqui o baralho dividido em dois, um direito e um esquerdo. " +
        " Qual e que vai escolher ? (Responda 'direito' ou 'esquerdo')! " }            
    ]
    #création deck
    card_deck = [i+1 for i in range(38)]

    if input_value not in inputs:
        inputs.append(input_value)
        print(inputs)
    else:
        pass

    if (len(inputs) == 1):        

        return msg[0]

    if (len(inputs) == 2):

        return msg[1]        
    
    if (len(inputs) == 3):
        while True:           
            try:
                if inputs[2] in card_deck:
                    print("Index ok dans les cartes!")
                break 
                    
            except IndexError:                
                del inputs[2]                
                return {"messages": "Deve escolher un numero entre 1 e 38! Qual e o seu numero ?"}

        return msg[2]

    if (len(inputs) == 4):
        #mélanger deck
        suf(card_deck)
        column = len(inputs[0])
        cut_point = int(inputs[2])
        while True:
            if inputs[3] == "direita" or "Direita":
                chosen_deck = card_deck[0:cut_point]  
                break

            if inputs[3] == "esquerda" or "Esquerda":
                chosen_deck = card_deck[cut_point:37] 
                break
        else:
            del inputs[3]
            print(inputs)
            return {"messages": "Deve escolher 'direita' ou 'esquerda' imperativamente!" +
            "Qual e a sua resposta?"} 
 
    #construire tableau
    def splitBy(li, n=1):
        return [li[i:i+n] for i in range(0, len(li), n)]

    column = len(inputs[0])
    print(column)   

    list_of_cards = []
    for i in chosen_deck:        
        obj = MajorArcana.objects.get(pk=i)
        card_img = obj.card_image
        list_of_cards.append("<td><img src= " + card_img + " alt='card' width = '30%' height = '30%'></td>")
    card_board = splitBy(list_of_cards, column)
    final_card_deck = []
    for i in card_board:
        l = ''.join(i)
        final_card_deck.append("<tr>" + l + "</tr>")
    print(final_card_deck)
    f = ''.join(final_card_deck)
    return {"messages" : "<table>" + f + "</table>"}

