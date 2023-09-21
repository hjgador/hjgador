#!/usr/bin/env python3
# Author : Hester Jane Gador
# Author ID: 103503207
# Date Created : 2023/09/21

import time


Countdown_value = int(input('Enter a number: ') )
if Countdown_value > 0:
    print(Countdown_value)
    time.sleep(1)
    Countdown_value -= 1

print('done.')