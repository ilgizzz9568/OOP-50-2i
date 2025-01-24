# декоратор без аргументов


def simple_dec (func):
    def wrapper():
        print('start')
        func()
        print('end')

    return wrapper

@simple_dec
def print_text():
    print('text')

print_text()



# декоратор с аргументами

def greeting_dec(func):
    def wrapper():
        print('hello')
        func()
        print('goodbye')
        