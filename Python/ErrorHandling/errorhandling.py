
print('-----*Error handling*-----')
def sum(num1, num2):
    try:
        return num1 + num2
    except TypeError as err:
        print(f'Error occured {err}')


sum(1,1)
sum(1, '3')


def getage():

    while True:
        try:
            age = int(input('Enter your age: '))
            # raise Exception('error occured')
            # raise ValueError('error occured')
        except ValueError:
            print('please enter correct age')
        # catch all other errors
        except BaseException as error:
            print(f'An exception occurred: {error}')
        else:
            print('thank you')
            break
        finally:
            print('finally done')



getage()

# catch all possible error
# try:
#     do_something()
# except:
#     print("Caught it!")

# try:
#     f = open('myfile.txt')
#     s = f.readline()
#     i = int(s.strip())
# except IOError as (errno, strerror): // ignore keyboard interrupt errors
#     print("I/O error({0}): {1}".format(errno, strerror))
# except ValueError:
#     print("Could not convert data to an integer.")
# except:
#     print("Unexpected error:", sys.exc_info()[0])
#     raise
#     



# import traceback
# 
# def bad_method():
#     try:
#         sqrt = 0**-1
#     except Exception:
#         print(traceback.print_exc())
# 
# bad_method()