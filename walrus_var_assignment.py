#!/usr/bin/env python3

import time


def count_odds(data):
    time.sleep(1)
    odds = [odd for odd in data if odd % 2 ==1]
    return len(odds)


data = [45, 67, 22, 43, 12]

# Start Time
t1 = time.time()

# if count_odds(data) > 1:
#     print(f"{count_odds(data)} odds")
# Walrus operator

if (num:=count_odds(data)) > 1:
    print(f"{num} odds")


# End Time
t2 = time.time()
print(f"Took {t2-t1} seconds.")
