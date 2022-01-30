

myfile = open('D:\\1_Learning\\C_C++\\Repo\\2021_10_18\\LearnCPlusPlus\\Python\\File_IO\\test.txt')

# read complete file
print(myfile.read())

# move cursor to first line
myfile.seek(0)
# read  line by line
print(myfile.readline())

# move cursor to first line
myfile.seek(0)
# get all lines as a list 
print(myfile.readlines())

# move cursor to first line
myfile.seek(0)
for line in myfile:
    print(line)

myfile.close()


# proper way to  handle file
filepath = 'D:\\1_Learning\\C_C++\\Repo\\2021_10_18\\LearnCPlusPlus\\Python\\File_IO\\test.txt'
with open(filepath) as myfile:
    print(myfile.readlines())

# proper way to  handle file
filepath = 'D:\\1_Learning\\C_C++\\Repo\\2021_10_18\\LearnCPlusPlus\\Python\\File_IO\\test.txt'
with open(filepath, mode='a') as myfile:
    myfile.write('written something new\n')
    
# proper way to  handle file
filepath = 'D:\\1_Learning\\C_C++\\Repo\\2021_10_18\\LearnCPlusPlus\\Python\\File_IO\\test.txt'
with open(filepath) as myfile:
    print(myfile.readlines())

# proper way to  handle file
filepath = 'D:\\1_Learning\\C_C++\\Repo\\2021_10_18\\LearnCPlusPlus\\Python\\File_IO\\test1.txt'
with open(filepath, mode='w') as myfile:
    myfile.write('new file created\n')

# mode ' r' will only read the file 
# mode 'r+' will read and overwrite the file
# mode 'w' will clear all existing data in file and insert new data and will also create new file if the given path doesn't exists
# mode 'a' will append