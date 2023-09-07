# A List is a kind of Collection

friends = ['Joseph', 'Glenn', 'Sally']
carryon = ['socks', 'shirt', 'perfume']



# List Constants
print([1, 24, 76])
print(['red', 'yellow', 'blue'])
print(['red', 24, 98.6])
print([1, [5, 6], 7])
print([])



# We already use lists!
for i in [5, 4, 3, 2, 1] :
    print(i)
print('Blastoff!')



# Lists and definite loops - best pals
friends = ['Joseph', 'Glenn', 'Sally']
for friend in friends :
    print('Happy New Year:', friend)
print('Done!')

z = ['Joseph', 'Glenn', 'Sally']
for x in z :
    print('Happy New Year:', x)
print('Done!')



# Looking Inside Lists
friends = ['Joseph', 'Glenn', 'Sally']
print(friends[1])



# Lists are Mutable - изменяємые
fruit = 'Banana'
try: fruit[0] = 'b'
except: print("TypeError: 'str' object does not support item assignment")
x = fruit.lower()
print(x)

lotto = [2, 14, 26, 41, 63]
print(lotto)
lotto[2] = 28
print(lotto)



# How Long is a List?
greet = 'Hello Bob'
print(len(greet))
x = [1, 2, 'joe', 99]
print(len(x))



# Using the range function
print(range(4))
friends = ['Josep', 'Glenn', 'Sally']
print(len(friends))
print(range(len(friends)))


# A tale  of two  loops...
friends = ['Josep', 'Glenn', 'Sally']
for friend in friends :
     print('Happy New Year:', friend)

for i in range(len(friends)) :
    friend = friends[i]
    print('Happy New Year:', friend)
