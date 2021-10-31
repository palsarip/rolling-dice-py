# [ROLLING DICE GAME by palsarip]

# [MODULE]
import random

# [VARIABLES]
y = 1
n = 2
min = 1
max = 12
min1 = 1
max2 = 12
player_result = ()
bot_result = ()
bot = ()

#[VARIABLES INPUT]
player = input("Input your name: ")
roll = input("Do you wanna roll the dice? (y/n): ")

# [CODES]
if roll == "y" or roll == "1":
    player_result = random.randint(min, max)
    bot_result = random.randint(min1, max2)
    if player_result > bot_result:
        print("---------------------------------")
        print(player + "'s dice = " + str(player_result))
        print("Bot's dice = " + str(bot_result))
        print(player + ' win!')
        print("---------------------------------")
    elif player_result == bot_result:
        print("---------------------------------")
        print(player + "'s dice = " + str(player_result))
        print("Bot's dice = " + str(bot_result))
        print("Draw!")
        print("---------------------------------")
    else:
        print("---------------------------------")
        print(player + "'s dice = " + str(player_result))
        print("Bot's dice = " + str(bot_result))
        print("Bot win!")
        print("---------------------------------")
elif roll == "n" or roll == "2":
    print(":(")
else:
    print("Please press y/n only")

