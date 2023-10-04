cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.

#Link: https://games.washingtonpost.com/games/blackjack/

import random
from replit import clear   
from art import logo

user_cards=[]
comp_cards=[]
game_end=False


'''Getting 2 random cards'''
for _ in range(2):
    user_cards.append(random.choice(cards))
    comp_cards.append(random.choice(cards))
def score_list(cards):
    '''Adding up the user's and the computer's scores'''
    if 10 in cards and 11 in cards:
        return ('Lose')
        
    if sum(cards) == 21 and len(cards) == 2:
        return 21
    
    if sum(cards)>21 and 11 in cards:
         cards.remove(11)
         cards.append(1)
    return sum(cards)


def compare(user_score,comp_score):
    '''Comparing user score with computer score to see if user score is higher'''
    if user_score>21 and comp_score>21:
        print("you lose")
        return True
        
    if user_score==comp_score:
        print("Draw")
        return True
        
    elif comp_score == 21:
        print ("Lose, opponent has Blackjack")
        return True
        
    elif user_score == 21:
        print ("Win with a Blackjack")
        return True
        
    elif user_score > 21:
        print ("You went over. You lose")
        return True
        
    elif comp_score > 21:
        print ("Opponent went over. You win")
        return True
        
    return False
    
def comp_score_fill_hand(user_score, comp_score):
    '''Computer plays, if score is less than 17, keep drawing cards'''
    print(type(comp_score),'comp_score')
    while comp_score<21:
        comp_cards.append(random.choice(cards))
        comp_score=score_list(comp_cards)
    print(f"Your final hand: {user_cards}, final score: {user_score}")
    print(f"Computer's final hand: {comp_cards}, final score:{comp_score}")
    compare(user_score, comp_score)
    
def game(user_cards, comp_cards, game_end):
    '''Starting of the game'''
    
    '''Calling function to add up scores'''
    user_score=score_list(user_cards)
    comp_score=score_list(comp_cards)
    
    while game_end != True:

        print(f"Your cards: {user_cards}, current score:{user_score}")
        print(f"Computer's first card: {comp_cards[0]}")
        if game_end != compare(user_score, comp_score):
            break


        '''Asking the user if they want to get another card (if True) Drawing another card'''
        user_decide=input("Type 'y' to get another card, type 'n' to pass: ")
        if user_decide=='y':
            user_cards.append(random.choice(cards))

        if user_decide == 'n':
            comp_score_fill_hand(user_score, comp_score)
            break
            
print (logo)
first=input('Do you want to play? ')

if first=='y':
    clear()
    game(user_cards, comp_cards, game_end)
    
second=input("Do you want to play again?")
if second=="y":
    user_cards2=[]
    comp_cards2=[]
    game_end2=False
    
    
    '''Getting 2 random cards'''
    for _ in range(2):
        user_cards2.append(random.choice(cards))
        comp_cards2.append(random.choice(cards))
    clear()
    game(user_cards2, comp_cards2, game_end2)
    
if second=='n':
    print('End')
    clear()
    