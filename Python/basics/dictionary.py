# dictionary
print('-------*dictionary basics*-------')
dictionary = {
    'a': 1,
    'b': 2,
    'c': 3
}

print(dictionary['b'])
print(dictionary)

newdictionary = {
    'a': [1, 3, 4, 5],
    'b': 'kalidas',
    'c': 'a'
}

print(newdictionary)

user = {
    'age': 25,
    'name': 'kalidas',
}

print(user['age'])
print(user.get('age'))
print(user.get('name'))

print('age' in user.keys())
print(25 in user.values())
print(user.items())

# add items
user.update({'school': 'sanjose'})
user['home'] = 'coimbatore'

print(user.items())
for item in user:
    print(item)


# delete items
user.pop('home')
print(user.items())

user.popitem() # delete the last item
print(user.items())

user.clear()
print(user.items())
