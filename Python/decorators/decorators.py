from time import time

def my_decorator(func):
    def wrap_func():
        print('***************')
        func()
        print('***************')
    return wrap_func


def new_decorator(func):
    def wrap_func(*args, **kwargs):
        print('################################')
        func(*args, **kwargs)
        print('################################')
    return wrap_func

@my_decorator
def hello():
    print ("Hellooooo")


@new_decorator
def new(x, emojis=None):
    print(x, emojis)


#  decorator super boosts the function
hello()
# result: 
# ***************
# Hellooooo
# ***************

new('kalidas', ':)')



def performance(func):
    def wrapper(*args, **kwargs):
        t1 = time()
        result = func(*args, **kwargs)
        t2 = time()
        print(f'took {t2-t1} seconds')
        return result
    return wrapper


@performance
def verybigfunction():
    for i in range(1000000):
        i = i * 1000


verybigfunction()