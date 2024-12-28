import time

def display_table_rules():
    print("The rules are simple:\nYou're playing against the dealer, trying to get as close to 21 as possible without going over.")
    time.sleep(.1)
    print("All face cards are worth 10 pts, and Aces are worth either an 11, or 1")
    time.sleep(.1)
    print("You can bet any amount, but you can't bet more than your current chips")
    time.sleep(.1)
    print("If you go over 21, you lose your bet.")
    time.sleep(.1)
    print("Odds are 2-1 for insurance and 3-2 for blackjack")
    time.sleep(.1)
    print("Good luck!\n")

def get_bet(player_chips):
    while True:
        try:
            bet = int(input("What would you like to bet?\n"))
            if bet <= 0 or bet > player_chips:
                print(f"Invalid bet. You have {player_chips} chips.")
                continue
            return bet
        except ValueError:
            print("Invalid input. Please enter a number.")


def handle_blackjack(player_hand, dealer_hand, bet, player_chips):
    print(f"Your hand is {player_hand}. Blackjack!")
    if eval_hand(dealer_hand) == "21":
        print(f"Dealer also has {dealer_hand}. It's a push!")
        player_chips += bet
    else:
        print(f"You win {1.5 * bet} chips!")
        player_chips += int(1.5 * bet)


def offer_insurance(dealer_hand, player_chips, bet):
    if dealer_hand[0].rank == "Ace" and player_chips >= bet // 2:
        while True:
            choice = input("Dealer shows an Ace. Would you like to buy insurance? (yes/no): ").lower()
            if choice == "yes":
                print("Insurance purchased!\n")
                break
            elif choice == "no":
                return 2
            print("Invalid input.")
        if eval_hand(dealer_hand) == "21":
            print("Dealer has blackjack! Insurance pays out.")
            return 1
        return 0
    return 5

def handle_dealer_blackjack(dealer_hand):
    if eval_hand(dealer_hand) == "21" and len(dealer_hand) == 2:
        print(f"Dealer has {dealer_hand}. Blackjack!")
        print("You lose your bet.")
        return True  # End the round
    return False

def handle_dealer_turn(dealer_hand, deck):
    print(f"Dealer's turn. Dealer flips: {dealer_hand[1]}")
    while int(eval_hand(dealer_hand)) < 17:
        dealer_hand.append(deck.draw())
        print(f"Dealer draws: {dealer_hand[-1]}")
    if int(eval_hand(dealer_hand)) > 21:
        print(f"Dealer busts!")
        return dealer_hand
    print(f"Dealer's final hand: {dealer_hand} ({eval_hand(dealer_hand)})")
    return dealer_hand


def handle_player_turn(split_hands, player_chips, deck, dealer_hand):
    i = 0
    while i < len(split_hands):
        hand, bet = split_hands[i]
        while True:
            print(f"Your current hand: {hand} ({eval_hand(hand)})")
            print(f"Dealer shows: {dealer_hand[0]}")
            action = input("Would you like to hit, stay, double down, or split? (h/s/dd/split): ").lower()
            print("\n")
            if action == "h":
                hand.append(deck.draw())
                print(f"You drew: {hand[-1]}")
                if eval_hand(hand) > "21":
                    break
            elif action == "s":
                print("Staying!")
                break
            elif action == "dd" and player_chips >= bet and len(hand) == 2:
                print("Doubling down!")
                player_chips -= bet
                hand.append(deck.draw())
                print(f"You drew: {hand[-1]}")
                split_hands[i][1] *= 2
                break
            elif action == "split" and len(hand) == 2 and hand[0].rank == hand[1].rank and player_chips >= bet:
                print("Splitting hand!")
                player_chips -= bet
                split_hands.append([[hand.pop(), deck.draw()], bet])  # Create the second hand
                split_hands[i] = [[hand[0], deck.draw()], bet]  # Update the original hand
                break
            else:
                print("Invalid choice or insufficient chips for this action.")
                continue
        split_hands[i] = [hand, bet]
        i += 1
    return split_hands

def resolve_bets(split_hands, dealer_hand, player_chips):
    dealer_total = int(eval_hand(dealer_hand))
    for hand, hand_bet in split_hands:
        player_total = int(eval_hand(hand))
        if player_total > 21:
            print("Bust!")
            print(f"You bust with {hand}.")
        elif dealer_total > 21 or player_total > dealer_total:
            print(f"You win with {hand}! Payout: {2 * hand_bet} chips.")
            player_chips += 2 * hand_bet
        elif player_total == dealer_total:
            print(f"Push with {hand}. Bet returned.")
            player_chips += hand_bet
        else:
            print(f"Dealer wins against {hand}.")
    return player_chips

def eval_hand(hand):
    total = 0
    aces = False
    for card in hand:
        rank = card.rank
        if rank in {"Jack", "Queen", "King"}:
            rank = 10
        elif rank == "Ace":
            aces = True
            rank = 1
        else:
            rank = int(rank)
        total += rank
    if aces and total + 10 < 21:
        return str(total + 10)
    return str(total)

def play_hand(hand, player_chips, bet, deck, dealer_hand):
    while int(eval_hand(hand)) < 21 and action == "h":
        print(f"Your current hand is {hand}.")
        print(f"You hand evaluates to {eval_hand(hand)}.")
        time.sleep(.1)
        print(f"The dealer shows {dealer_hand[0]}")
        print("Would you like to hit or stay?")
        action = input("h/s? ")
        while action not in {"h", "s"}:
            print("Invalid input.")
            action = input("h/s? ")
        if action == "h":
            print("Hitting!")
            hand.append(deck.draw())
            print(f"You drew the {hand[-1]}")
        else:
            print("Staying!")
            break
    return hand