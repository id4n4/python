import random

suits = ["Hearts", "Spades", "Clubs", "Diamonds"]
ranks = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King", "Ace"]
cards = []

for suit in suits:
    for rank in ranks:
        cards.append(f'{rank} of {suit}')
longitud_cartas = len(cards)
print(f'there are {longitud_cartas} in the deck.')
print('dealing ...')
baraja = []
cont = 0
limite = 51
while len(baraja) <5:
    
    r = random.randint(0,limite)
    baraja.append(cards.pop(r))
    cont += 1
    limite -= 1

print(f'There are {limite+1} cards in the deck.')
print(f'Player has the following cards in their hand:')
print(baraja)
