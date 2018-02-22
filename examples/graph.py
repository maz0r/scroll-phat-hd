#!/usr/bin/env python

import time
import random

import scrollphathd

print("""
Scroll pHAT HD: Graph

Displays a graph with random values.

Press Ctrl+C to exit!

""")

MIN_VALUE = 0
MAX_VALUE = 50

scrollphathd.rotate(180)

# Begin with a list of 15 zeros
values = [0] * scrollphathd.DISPLAY_WIDTH

while True:
    # Insert a random value at the beginning
    values.insert(0, random.randrange(MIN_VALUE, MAX_VALUE))

    # Get rid of the last value, keeping the list at 15 (DISPLAY_WIDTH) items
    values = values[:scrollphathd.DISPLAY_WIDTH]

    # Plot the random values onto Scroll pHAT HD
    scrollphathd.set_graph(values, low=MIN_VALUE, high=MAX_VALUE, brightness=0.3)

    scrollphathd.show()
    time.sleep(0.05)
