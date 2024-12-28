import time
from src import *

def main():
    print("Howdy! Welcome to Cole's Terminal Blackjack Game, I'll be your dealer today!\n")
    time.sleep(0.1)
    display_table_rules()

    player_chips = 1000
    print(f"You will start out with {player_chips} chips.\n")
    time.sleep(0.1)

    deck = Deck()
    while player_chips > 0:
        if deck.len() < 30:
            print("Shuffling deck...")
            deck = Deck()
            time.sleep(0.1)

        print(f"You have {player_chips} chips.")
        bet = get_bet(player_chips)
        player_chips -= bet

        print("\nDealing...")
        player_hand = [deck.draw(), deck.draw()]
        dealer_hand = [deck.draw(), deck.draw()]
        time.sleep(0.1)

        if eval_hand(player_hand) == "21" and eval_hand(dealer_hand) == "21":
            print("Player and Dealer blackjack.")
            print("Push")
            continue
        elif eval_hand(player_hand) == "21":
            handle_blackjack(player_hand, dealer_hand, bet, player_chips)
            continue

        insurance = offer_insurance(dealer_hand, player_chips, bet)
        if insurance == 0:
            player_chips -= bet // 2
            print("Insurance purchased")
            print("Dealer does not have blackjack.\n")
        elif insurance == 1:
            print("Insurance purchased")
            print("Dealer blackjack")
            print("Insurance pays 2-1")
            player_chips += bet
            continue

        if handle_dealer_blackjack(dealer_hand):
            continue

        split_hands = [[player_hand, bet]]
        split_hands = handle_player_turn(split_hands, player_chips, deck, dealer_hand)

        dealer_hand = handle_dealer_turn(dealer_hand, deck)
        player_chips = resolve_bets(split_hands, dealer_hand, player_chips)

        print(f"End of round. You have {player_chips} chips remaining.\n")
        time.sleep(0.5)

    print("Game over! You ran out of chips.")

if __name__ == "__main__":
    main()
