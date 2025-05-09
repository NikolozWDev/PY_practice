# decorators
def who_is(func):
    def wrapper(*args, **kwargs):
        print('wrapper1')
        func(*args, **kwargs)
    return wrapper

def who_is_2(func):
    def wrapper(*args, **kwargs):
        print('wrapper2')
        func(*args, **kwargs)
    return wrapper

@who_is
@who_is_2
def give_away(par):
    return f'Here your {par}'

print(give_away('something'))



# exception handling
try:
    num = int(input('Enter number (1 / n): '))
    print(1 / num)
except ZeroDivisionError:
    print('ZeroDivisionError: you cant enter 0')
except ValueError:
    print('ValueError: you can enter only numbers')
except Exception:
    print('Something want wrong')
finally:
    print('do some cleanup')