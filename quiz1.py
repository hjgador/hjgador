#!/usr/bin/env python3
# Author : Hester Jane Gador
# Author ID: 103503207
# Date Created : 2023/09/21

import time

def countdown():
    seconds = int(input("enter the number: "))
    while seconds > 0:
        print(seconds)
        time.sleep(1)
        seconds-= 1
              
countdown()
print("done.")