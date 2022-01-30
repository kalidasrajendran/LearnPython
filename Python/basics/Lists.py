print('-------*-------')
listname = ['kali', 'ramya', 'sajai']

for name in listname:
    print(name)
print('-------*-------')

print('-------*-------')
list1 = ['kali', 1, 2, 'a']
for name in list1:
    print(name)
print('-------*-------')

# list as array
print('-------*list as array*-------')
list1 = ['zero', 1, 2, 'three']
for x in range(len(list1)):
    print(list1[x])

print('-------*-------')

# list slicing
print('-------*list slicing*-------')

list1 = ['zero', 1, 2, 'three']
print(list1[0:2])
print(list1[0:])
print(list1[0::2])
print(list1[::-1])

print('-------*-------')

# list reverse
print('-------*list reverse*-------')

list1 = ['zero', 1, 2, 'three']

print(list1[::-1])

print('-------*-------')

# list sort
print('-------*list sort*-------')

list1 = [0, 2, 1, 0]
list1.sort()

print(list1)

print('-------*-------')

# list copying and modifying
print('-------*list copying and modifying*-------')

list1 = [0, 2, 1, 0]
list2 = list1
list3 = list1[:]

# list copying
print('-------*list copying*-------')
print(list1)
list3[0] = 10
print(list3)
print(list1)

# list modifying
print('-------*list modifying*-------')
print(list1)
list2[0] = 10
print(list2)
print(list1)

print('-------*-------')

# Copy a List
print('-------*Copy a List*-------')
basket = ['apples', 'pears', 'oranges']
new_basket = basket.copy()
new_basket2 = basket[:]
print(new_basket)
print(new_basket2)

# Index
print('-------*Index of a List*-------')
basket = ['a', 'x', 'b', 'c', 'd', 'e']
print(basket.index('d'))
print(basket.index('d', 0, len(basket)))
print('d' in basket)
print('s' in basket)
print(basket)

# sort and reverse
print('-------*sort and reverse*-------')
basket = ['a', 'x', 'b', 'c', 'd', 'e']
print(basket)
basket.sort(reverse=1)
print(basket)
basket = ['a', 'x', 'b', 'c', 'd', 'e']
basket.reverse()
print(basket)

# range
print('-------*range*-------')
print(list(range(0, 100)))


# join
print('-------*join*-------')
sentence = ' '
new_sentence = sentence.join(['hi', 'my', 'name', 'is', 'kalidas'])
print(new_sentence)

sentence = '#'
new_sentence = sentence.join(['hi', 'my', 'name', 'is', 'kalidas'])
print(new_sentence)

sentence = ';'
new_sentence = sentence.join(['hi', 'my', 'name', 'is', 'kalidas'])
print(new_sentence)

new_sentence = ' '.join(['hi', 'my', 'name', 'is', 'kalidas'])
print(new_sentence)

new_sentence = ' kali '.join(['hi', 'my', 'name', 'is', 'kalidas'])
print(new_sentence)

# list unpacking
print('-------*list unpacking*-------')
a, b, c, *other = [1, 2, 3, 4, 5, 6, 7, 8]
print(a)
print(b)
print(c)
print(other)

# Append Items
print('-------*Append Items*-------')
thislist = ["apple", "banana", "cherry"]
thislist.append("orange")
print(thislist)

# Insert  Items
print('-------*Insert Items*-------')
thislist = ["apple", "banana", "cherry"]
thislist.insert(1, "orange")
print(thislist)

# extend  Items
print('-------*extend Items*-------')
thislist = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]
thislist.extend(tropical)
print(thislist)
