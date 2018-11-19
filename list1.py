weekday = [1, 2, 3]
print(weekday[1])

fruit = ['pineapple', 'pear']
fruit.insert(1, 'grape')
print(fruit)

fruit[0:0] = ['Orange']
print(fruit)

# key_test = {[]: 'a Test'}
# print(key_test)

NASDAQ_code = {'BIDU':'Baidu', 'SINA':'Sina'}
print(NASDAQ_code)

NASDAQ_code['YOKU'] = 'Youku'
print(NASDAQ_code)

NASDAQ_code.update({'FB':'Facebook', 'TSLA':'Tesla'})
print(NASDAQ_code)

a_set = {1, 2, 3, 4}
a_set.add(5)
print(a_set)