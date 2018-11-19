search = '168'
num_a = '1386-168-0006'
num_b = '1681-222-0006'

print(search + ' is at ' + str(num_a.find(search)) + ' to '+ str(num_a.find(search) + len(search)) + ' of num_a')
print(search + ' is at ' + str(num_b.find(search)) + ' to '+ str(num_b.find(search) + len(search)) + ' of num_b')

print('{} a world she can get what she {} for.'.format('With', 'came'))
print('{preposition} a world she can get what she {verb} for.'.format(preposition = 'With', verb = 'came'))
print('{0} a world she can get what she {1} for.'.format('With', 'came'))