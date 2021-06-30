import random

def play():

    user = input("What's your choice? 'r' for rock, 'p' for paper, 's' for scissors, and 'q' for quit\n")

    bot = random.choice(['r', 'p', 's'])
    print("I choose " + bot)

    if user == bot:
         return 'It\'s a tie'

    if winner(user, bot):
         return 'You won!'

    return 'Oop\'s You lost!'

def winner(user, bot):
    if (user == 'r' and bot == 's') or (user == 's' and bot == 'p') or (user == 'p' and bot == 'r'):
        return True


print(play())
