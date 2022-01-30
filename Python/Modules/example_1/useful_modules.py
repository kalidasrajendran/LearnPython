from collections import Counter, defaultdict, OrderedDict

mylist = [10, 20, 30, 40, 50, 60, 60, 10]
mydict = Counter(mylist)
print(mydict) # create a dictionary with number of occurances for each elements

mysentence = 'I am kalidas'
print(Counter(mysentence)) # create a dictionary with number of occurances for each elements

print('kalidas')

sampledict = defaultdict(int, {'a': 1, 'b': 2, 'c': 3, 'd': 4})
print(sampledict['a']) # defaul dictionary returns a specified default value if the key doesn't exists

sampledict = OrderedDict()
sampledict['a'] = 3
sampledict['c'] = 4
sampledict['e'] = 1
sampledict['d'] = 2
sampledict['b'] = 5

print(sampledict)
# OrderedDict iterates over keys and values in the same order that the keys were inserted. 
# If a new entry overwrites an existing entry, then the order of items is left unchanged.
# If an entry is deleted and reinserted, then it will be moved to the end of the dictionary.