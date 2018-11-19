import random
def roll_dice(numbers=3, points=None):
    print('<<<< ROLL THE DICE! >>>>')
    if points is None:
        points = []
    while numbers > 0:
        point = random.randrange(1, 7)
        points.append(point)
        numbers = numbers - 1
    return points

def roll_result(total):
    isBig = 11 <= total <=18
    isSmall = 3 <= total <=10
    if isBig:
        return 'Big'
    elif isSmall:
        return 'Small'

def start_game():

    amount = 5000
    while amount > 0:
        print('<<<< GAME STARTS! >>>>')
        choices = ['Big', 'Small']
        your_choice = input('Big or Small :')
        your_coin = int(input('How much you wanna bet ?'))
        # amount = amount - your_coin
        if your_choice in choices:
            points = roll_dice()
            total = sum(points)
            youWin = your_choice == roll_result(total)
            if youWin:
                print('The points are ', points, 'You Win!')
                amount = amount + your_coin * 2
                print('Your current coin :' + str(amount))
            else:
                print('The points are', points, 'You lose !')
                amount = amount - your_coin
                print('Your current coin :' + str(amount))
        else:
            print("Invalid Words")
            start_game()
    print('<<<< GAME OVER! >>>>')

start_game()