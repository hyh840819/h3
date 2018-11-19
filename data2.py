num_list = [5,3,56,3,6,33,67,3]
print(sorted(num_list))
print(sorted(num_list,reverse=True))

a = []
for i in range(1,11):
    a.append(i)

print(a)

b = [i for i in range(1, 11)]
print(b)

# for a,b in zip(num,str)
#     print(b, 'is', a)

c = [i**2 for i in range(1, 10)]
print(c)

d = [j+1 for j in range(1, 10)]
print(d)

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
for num,letters in enumerate(letters):
    print(letters, 'is' ,num+1)

