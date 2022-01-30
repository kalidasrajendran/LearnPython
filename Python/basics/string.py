print(type('kalidas'))

usename = 'kalidas'
password = 'secret'

# three single quotes for long string
longstring = '''
WOW
o o
---
'''

print(longstring)

firstname = 'kalidas'
lastname = 'Rajendran'
fullname = firstname + ' ' + lastname
print(fullname)


# type conversions
a = 10

c = str(a)
print('age is : ' + c)

# escape sequences
weather = 'it\'s kind of \"sunny\"'
print(weather)

# formatted strings
name = 'kalidas'
age = 30
print(f'hi {name} you are {age} years old')

# String indexes
name = 'kalidas'
for s in name:
    print(s)

# [start:stop]
print(name[0:2])

# [start:stop:stepover]
print(name[0:6:2])

print(name[-1])

# reverse a string
print(name[::-1])

type('Hellloooooo') # str

'I\'m thirsty'
"I'm thirsty"
"\n" # new line
"\t" # adds a tab

'Hey you!'[4] # y
name = 'Andrei Neagoie'
name[4]     # e
name[:]     # Andrei Neagoie
name[1:]    # ndrei Neagoie
name[:1]    # A
name[-1]    # e
name[::1]   # Andrei Neagoie
name[::-1]  # eiogaeN ierdnA
name[0:10:2]# Ade e
# : is called slicing and has the format [ start : end : step ]

'Hi there ' + 'Timmy' # 'Hi there Timmy' --> This is called string concatenation
'*'*10 # **********



# Basic Functions
len('turtle') # 6

# Basic Methods
'  I am alone '.strip()               # 'I am alone' --> Strips all whitespace characters from both ends.
'On an island'.strip('d')             # 'On an islan' --> # Strips all passed characters from both ends.
'but life is good!'.split()           # ['but', 'life', 'is', 'good!']
'Help me'.replace('me', 'you')        # 'Help you' --> Replaces first with second param
'Need to make fire'.startswith('Need')# True
'and cook rice'.endswith('rice')      # True
'bye bye'.index('e')                  # 2
'still there?'.upper()                # STILL THERE?
'HELLO?!'.lower()                     # hello?!
'ok, I am done.'.capitalize()         # 'Ok, I am done.'
'oh hi there'.find('i')               # 4 --> returns the starting index position of the first occurrence
'oh hi there'.count('e')              # 2


print('-------*-------')
name = 'Kalidas,Rajendran'
arrayname = name.split(',')
for name in arrayname:
    print(name)
print('-------*-------')



