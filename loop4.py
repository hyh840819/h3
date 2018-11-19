
even_num = int(input('Your even num: '))

def even_number(even_num):
    for i in range(1, even_num + 1):
        if i % 2 == 0:
            print(i)

even_number(even_num)