
try:
    filepath = 'D:\\1_Learning\\C_C++\\Repo\\2021_10_18\\LearnCPlusPlus\\Python\\File_IO\\test3.txt'
    with open(filepath) as myfile:
        print(myfile.readlines())
except FileNotFoundError as err:
    print('file not found', err)
except IOError as err:
    print('IO error occured', err)