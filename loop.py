for every_letter in 'Hello World':
    print(every_letter)



for i in range(1, 10):
    for j in range(1, 10):
        print('{} X {} = {}'.format(i,j,i*j))


# while 1 < 3:
#     print('1 is smaller than 3')


count = 0
while True:
    print('Repeat this line !')
    count = count + 1
    if count == 5:
        break