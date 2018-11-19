amount = int(input('principle amount: '))
rate = float(input('rate: '))
time = int(input('year: '))

def invest(amount, rate, time):
    for i in range(1, time):
        amount = amount * rate + amount
        print("year" + str(i) + ' $' + str(amount))
        i = i + 1

invest(amount, rate, time)