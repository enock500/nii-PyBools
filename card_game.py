#!/usr/bin/env python3
"""
A simple simulated card game involving two players named
James and Jane.

James's strategy is as follows  lefor all games:
- Play the cards in the following order: 1st, 3rd, 5th, 2nd and 4th

Jane's strategy is as follows for all games:
- Play the cards in the following order: 5th, 1st, 2nd, 4th, and 3rd

Both players stick to their strategies no matter what cards
they are dealt.

James won a coin toss and will play the first card to begin the game.

The algorithm (logic) is as follows:
1. Check the value of player1's card to see if it's greater than or equal to player2's card and save the result of that check to a boolean variable.
2. Manually compute the result of the first round to determine who plays first during the next round. If the result of the first round is `True`, then player1 starts the next round again. 
Otherwise, player2 will start the next round.
3. Repeat steps 1 and 2 until both players have played all their cards in the order of their strategies.
4. The person who wins the most rounds, wins the game.
5. Set the variable `winner` to the name of the winner (through the appropriate player variable below) at the end of each game, and increment the `game` variable to signify the start of the next game.
6. Repeat the algorithm until all 3 games have been played and an overall winner can be determined.
7. Print the name of the overall winner to the terminal.
"""

# Declare two variables `player1` and `player2` and set them as the
# names of the players in the game.
player1 = "James"
player2 = "Jane"
# Declare each of the suits (clubs, diamonds, hearts, and spades) as an int variable and set its value to its appropriate numerical value.
# (Remember: Each suit is given a numerical value based on the numerical equivalent of the letter it begins with. See the assignment overview
# for more details on this)
clubs = 3
diamonds = 4
hearts = 8
spades = 19 



# Declare a variable `game` of type int and set it to the first round
# The games will be incremented by one after each game, by computing:




# For game 1:
# James is dealt the following cards: 5 Hearts, 3 Clubs, Ace Clubs, King Diamonds, 2 Diamonds
# Jane is dealt the following cards: 2 Spades, Queen Spades, 10 Diamonds, 7 Clubs , Jack Hearts

#Round 1

Jack = 11
Queen = 12
King = 13
Ace = 14

# Declare a list for James's cards and save it to the variable `James_cards`
# Declare another list for Jane's cards and save it to the variable `jane_cards`
# For each list, recall that the number on each card is added to the numerical value of its suit to determine how many points it's worth.
# eg. 5 of hearts will be worth 13 points and so the entry in the list will be 5 + <the numerical value of hearts>.
#  Note: DO NOT COMPUTE THESE BY HAND. Rather, use the variables you declared above!
James_cards = [
    5 + hearts,
    3 + clubs,
    Ace + clubs,
    King + diamonds,
    2 + diamonds,
]

Jane_cards = [
    2 + spades,
    Queen + spades,
    10 + diamonds,
    7 + clubs,
    Jack + hearts,
]

# Based on their strategies, play all 5 rounds of the game, and determine the winner at the end of the game.
# Set the variable `winner` to the name of the winner (through the appropriate player variable above) at the end of the game,
# Increment the `game` variable to signify the start of the next game.
game = 1
round_1 = (James_cards[0] >= Jane_cards[4])
print(round_1)
round_2 = (Jane_cards[0] >= James_cards[2])
print(round_2)
round_3 = (Jane_cards[1] >= James_cards[4])
print(round_3)
round_4 = (Jane_cards[3] >= James_cards[1])
print(round_4)
round_5 = (Jane_cards[2] >= James_cards[3])
print(round_5)


winner = player2
print(winner, "you won game 1") 


# #Incrementation of game 
game = game + 1




# For game 2:
# James is dealt the following cards: 7 Clubs, 5 Spades, 2 Hearts, Jack Clubs, 2 Spades
# Jane is dealt the following cards: Jack Hearts, King Diamonds, 8 Clubs, 9 Hearts , 7 Spades

James_cards = [
    7 + clubs,
    5 + spades,
    2 + hearts,
    Jack + clubs,
    2 + spades,
 ]

Jane_cards = [
    Jack + hearts,
    King + diamonds,
    8 + clubs,  
    9 + hearts, 
    7 + spades,
]

# Follow the same algorithm to determine the winner of this game
# Don't forget to increment the game variable!
game = 2
round_1 = (James_cards[0] >= Jane_cards[4])
print(round_1)
round_2 = (Jane_cards[0] >= James_cards[2])
print(round_2)
round_3 = (Jane_cards[1] >= James_cards[4])
print(round_3)
round_4 = (James_cards[1] >= Jane_cards[3])
print(round_4)
round_5 = (James_cards[3] >= Jane_cards[2])
print(round_5)

winner = player1
print(winner, "you won game 2")

# #Incrementation of game 
# game = game + 1
# # For game 3:
# # James is dealt the following cards: 10 Diamonds, 2 Clubs, 3 Spades, 7 Diamonds, 4 Spades
# # Jane is dealt the following cards: Queen Hearts, 9 Diamonds, 4 Hearts, 2 Diamonds , Queen Hearts
# James_cards = [
#     10 + diamonds,
#     2 + clubs,
#     3 + spades,
#     7 + diamonds,
#     4 + spades,
# ]

# Jane_cards = [
#     Queen + hearts,
#     9 + diamonds,
#     4 + hearts,
#     2 + diamonds,
#     Queen + hearts,
# ]

# # Follow the same algorithm to determine the winner of this game
# # Print the value of the game variable to signify the end of the game
# game = 3

# round_1 = (James_cards[0] >= Jane_cards[0])
# round_2 = (James_cards[1] >= Jane_cards[1])
# round_3 = (James_cards[2] >= Jane_cards[2])
# round_4 = (James_cards[3] >= Jane_cards[3])
# round_5 = (James_cards[4] >= Jane_cards[4])


# print(round_1)
# print(round_2)
# print(round_3)
# print(round_4)
# print(round_5)

# winner = player1
# print(winner, "you won game 3")  
# # Declare a variable `overall_winner` and set it equal to the player who won the most out of all 3 games
# # Set this variable through the player number variable. Print the value of this variables.....
# overall_winner = player2
# print(overall_winner, "declared winner")
