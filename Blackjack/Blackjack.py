import random
from art import logo
from replit import clear

blackjack = False
if input("Você quer jogar Blackjack? Digite 'y' ou 'n': ") == "y":
    blackjack = True

while blackjack:
    # Cartas Disponives
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

    # Cartas do Jogador
    user_cards = []

    # Cartas do Dealer
    dealer_cards = []

    # Sorteio das cartas para cada jogador
    def deal_cards(random_user_cards, random_dealer_cards):
        random_user_cards = random.sample(cards, 2)
        random_dealer_cards = random.sample(cards, 2)

        user_cards.extend(random_user_cards)
        dealer_cards.extend(random_dealer_cards)
    deal_cards(user_cards, dealer_cards)

    # Cálculo total das cartas
    def calculate_score(cards):
        score = sum(cards)
        if score > 21 and 11 in cards:
            cards.remove(11)
            cards.append(1)
            score = sum(cards)
        return score
    
    # Continuar jogando?
    def keep_playing():
        if input("Deseja continuar jogando digite [y/n]: ") == "y":
            clear()
            return blackjack == True
        else:
            clear()
            print("\nObrigado por jogar ;D")
            return blackjack == False

    # Total dos jogadores
    dealer_total = calculate_score(dealer_cards)
    user_total = calculate_score(user_cards)

    print(logo)
    while user_total < 21:
        print(f"Suas Cartas: {user_cards}, Seu total: {user_total}")
        print(f"Primeira carta do Dealer: {dealer_cards[0]}")
        if input("Digite 'y' para pegar outra carta, Digite 'n' para passar: ").lower() == "y":
            new_user_card = random.sample(cards, 1)
            user_cards.extend(new_user_card)
            user_total = calculate_score(user_cards)
            clear()
        else:
            break

    while dealer_total < 18:
        new_dealer_card = random.sample(cards, 1)
        dealer_cards.extend(new_dealer_card)
        dealer_total = calculate_score(dealer_cards)

    # Resultado
    def result():
        clear()
        print("--------------|RESULTADO|--------------")
        print(f"\nSuas Cartas {user_cards}, Seu Total: {user_total}")
        print(f"\nCartas do Dealer {dealer_cards}, Total do Dealer: {dealer_total}")

    # Condições do Vencedor
    def compare(user, dealer):
        global blackjack
        if user > 21 and dealer > 21:
            result()
            print("\nOs dois ultrapassaram 21 pontos, Empate!")
            blackjack = keep_playing()
        elif user > 21:
            result()
            print("\nVocê ultrapassou 21 pontos. Você Perdeu!")
            blackjack = keep_playing()
        elif dealer > 21:
            result()
            print("\nO Dealer ultrapassou 21 pontos. Você Venceu!")
            blackjack = keep_playing()
        elif user > dealer:
            result()
            print("\nVocê Venceu!")
            blackjack = keep_playing()
        elif dealer > user:
            result()
            print("\nVocê Perdeu!")
            blackjack = keep_playing()
        else:
            result()
            print("\nEmpate!")
            blackjack = keep_playing()

    compare(user_total, dealer_total)