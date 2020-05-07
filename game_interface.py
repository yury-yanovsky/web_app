import random
from deck import DECK


def humanise(card_object):
    return card_object.value.capitalize() + ' ' + card_object.suit.capitalize()


def get_stake():
    while True:
        stake = input()
        try:
            stake = int(stake)
            break
        except ValueError:
            if stake.lower() == 'exit':
                print('Close app? (y - yes)\n>>>', end='')
                if input() == 'y':
                    exit(0)
                print('Invalid stake, please try again\n>>>', end='')
    return stake


player_money = 100

while True:
    random.shuffle(DECK)
    dealer_hand = []
    player_hand = []

    dealer_hand.append(DECK.pop(0))
    player_hand.append(DECK.pop(0))
    dealer_hand.append(DECK.pop(0))
    player_hand.append(DECK.pop(0))

    while True:
        print(f'\nYour current money: {player_money}')
        print('Enter your stake\n>>>', end='')
        player_stake = get_stake()
        if player_stake <= 0.000000000000001 or player_stake > player_money:
            print('Invalid number, please try another one\n>>>')
            player_stake = get_stake()
        player_money -= player_stake
        print(f'Stake taken, your money: {player_money}')
        decision = ''
        while True:
            player_hand_h = list(map(humanise, player_hand))
            print(f'''
-----------------------------------------------------------------------------
First dealer`s card: {humanise(dealer_hand[0])}
Your cards: {'; '.join(player_hand_h)}
-----------------------------------------------------------------------------

Type your decision: "go" for another card, "double" to double the stake, "stop" to check cards, "pass" for new round
>>>''', end='')
            decision = input()
            if decision == 'go':
                player_hand.append(DECK.pop(0))
            elif decision == 'double':
                player_hand.append(dealer_hand.pop(0))
                dealer_hand.append(DECK.pop(0))
            elif decision == 'stop':
                pass_f = False
                break
            elif decision == 'pass':
                pass_f = True
                break

        player_sum = 0
        for card in player_hand:
            player_sum += card.compare_value
            if player_sum > 21:
                for checked_card in player_hand:
                    if checked_card.value == 'ace':
                        checked_card.compare_value = 1
        player_sum = 0
        for card in player_hand:
            player_sum += card.compare_value
        if player_sum > 21:
            print('You`ve lost, but maybe you`ll be luckier next time!')
            print('Dealer`s cards were:')
            print(' | '.join(list(map(humanise, dealer_hand))))
            print('\n Your cards were:')
            print(' | '.join(list(map(humanise, player_hand))))
            break
        elif player_sum == 21:
            print('Blackjack! You`ve won!')
            player_money += player_stake * 2
            print('Dealer`s cards were:')
            print(' | '.join(list(map(humanise, dealer_hand))))
            print('\n Your cards were:')
            print(' | '.join(list(map(humanise, player_hand))))
        elif player_sum < 21:
            dealer_sum = 0
            for card in dealer_hand:
                dealer_sum += card.compare_value
            while dealer_sum < 17:
                dealer_hand.append(DECK.pop(0))
                dealer_sum += dealer_hand[-1].compare_value
            if dealer_sum > 21:
                for checked_card in dealer_hand:
                    if checked_card.value == 'ace':
                        checked_card.compare_value = 1
                dealer_sum = 0
                for card in dealer_hand:
                    dealer_sum += card.compare_value
            if dealer_sum > 21:
                print('You`ve won!')
                print('Dealer`s cards were:')
                print(' | '.join(list(map(humanise, dealer_hand))))
                print('\n Your cards were:')
                print(' | '.join(list(map(humanise, player_hand))))
                player_money += player_stake * 2
            elif dealer_sum == 21:
                print('Dealer has blackjack. You`ve lost.')
                print('Dealer`s cards were:')
                print(' | '.join(list(map(humanise, dealer_hand))))
                print('\n Your cards were:')
                print(' | '.join(list(map(humanise, player_hand))))
            elif dealer_sum < 21:
                if dealer_sum < player_sum:
                    print('You`ve won!')
                    player_money += player_stake * 2
                    print('Dealer`s cards were:')
                    print(' | '.join(list(map(humanise, dealer_hand))))
                    print('\n Your cards were:')
                    print(' | '.join(list(map(humanise, player_hand))))
                else:
                    print('You`ve lost, but maybe you`ll be luckier next time!')
                    print('Dealer`s cards were:')
                    print(' | '.join(list(map(humanise, dealer_hand))))
                    print('\n Your cards were:')
                    print(' | '.join(list(map(humanise, player_hand))))
            break
        break
