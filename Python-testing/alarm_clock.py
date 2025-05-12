import time
import datetime

def alarm_clock(var_clock):
    is_running = True
    while is_running:
        current_time = datetime.datetime.now().strftime("%H:%M:%S")
        if var_clock < current_time:
            print('Error time')
            is_running = False
        print(current_time)
        if current_time == var_clock:
            print('Wake Up!')
            is_running = False
        time.sleep(1)


clock = input('set alarm clock (HH:MM:SS): ')
print(alarm_clock(clock))