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




# dates & times
import datetime

today = datetime.date.today()
print(today)
time = datetime.time(12, 4, 5)
print(time)
now = datetime.datetime.now()
print(now)



# multithreading
import threading
import time

def connect_server1():
    time.sleep(5)
    print('connected server 1')

def connect_server2():
    time.sleep(3)
    print('connected server 2')

def connect_server3():
    time.sleep(6)
    print('connected server 3')

chore1 = threading.Thread(target=connect_server1)
chore2 = threading.Thread(target=connect_server2)
chore3 = threading.Thread(target=connect_server3)

chore1.start()
chore2.start()
chore3.start()

chore1.join()
chore2.join()
chore3.join()



# request API data
import requests

def get_film_info(name):
    api_key = 'f6b6ef1b'
    url = f'http://www.omdbapi.com/?apikey={api_key}&t={name}'
    response = requests.get(url)
    data = response.json()
    return data

movie_title = input('Enter movie title: ')
print(get_film_info(movie_title))