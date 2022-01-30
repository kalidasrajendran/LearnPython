# print('Kalidas')
# name = 'kalidas'
# # name = input('what is your name: ')
# print('hello  ' + name)
#
# #fundamental datatypes
# a = 5+3
# print(a)
#
# print(type(2+4))
# print(type(2/4))
# print(type(2*4.2))
#
#
# int b = 10;

# list all contents in a folder
import os

# D:\volumeE_Contents
# python -c "import main; main.list_all_files('D:\volumeE_Contents')"

filecount = 0


def list_all_files(path):
    global filecount
    try:
        if os.path.exists(path):
            files = os.listdir(path)

            for f in files:
                pathname = os.path.join(path, f)
                filecount += 1
                if os.path.isfile(pathname):
                    print('This is a file: ' + pathname)
                else:
                    print('This is a folder: ' + pathname)
                    list_all_files(pathname)
    except TypeError as err:
        print('Error occurred: ' + err)


# directory_path = input('please give the path of the direcory: ')
directory_path = 'D:\\volumeE_Contents'
print(directory_path)

list_all_files(directory_path)
print('files count: ' + str(filecount))
