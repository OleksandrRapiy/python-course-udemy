import time
import os
from time import localtime

FILE_PATH = 'files/supa_druppa.txt'

# print(f'Current time {localtime().tm_sec}')
# time.sleep(10)
# print(f'Current time {localtime().tm_sec}')


while True: 
    if os.path.exists(FILE_PATH):
        with open(FILE_PATH) as file: 
            print(file.read())
    else: 
        print(f'[{localtime().tm_hour}:{localtime().tm_min}] There is no such file: {FILE_PATH}, ', )

    time.sleep(10)