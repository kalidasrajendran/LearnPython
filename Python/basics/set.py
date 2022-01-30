print('set')

my_set = {1, 2, 4, 5}  # only unique variables
my_set.add(100)

print(my_set)

# acces sets
print('-------*access values*-------')
thisset = {"apple", "banana", "cherry"}

for x in thisset:
    print(x)

# add items
print('-------*add items*-------')
thisset = {"apple", "banana", "cherry"}
thisset.add("orange")

print(thisset)

# combine 2 sets
print('-------*combine 2 sets*-------')
thisset = {"apple", "banana", "cherry"}
tropical = {"pineapple", "mango", "papaya"}
thisset.update(tropical)
print(thisset)

set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set1 = set1.union(set2)
print(set1)

# remove item
print('-------*remove items*-------')
thisset = {"apple", "banana", "cherry"}

thisset.remove("banana")
thisset.discard("apple")

print(thisset)

# methods
my_set = {1, 2, 3, 4, 5}
your_set = {4, 5, 6, 7, 8, 9, 10}

print('-------*difference*-------')
print(my_set.difference(your_set))

print(my_set & your_set)
print(my_set | your_set)

print('-------*intersection*-------')
print(my_set.intersection(your_set))


# set1 = {1,2,3}
# set2 = {3,4,5}
# set3 = set1.union(set2)               # {1,2,3,4,5}
# set4 = set1.intersection(set2)        # {3}
# set5 = set1.difference(set2)          # {1, 2}
# set6 = set1.symmetric_difference(set2)# {1, 2, 4, 5}
# set1.issubset(set2)                   # False
# set1.issuperset(set2)                 # False
# set1.isdisjoint(set2)                 # False --> return True if two sets have a null intersection.
