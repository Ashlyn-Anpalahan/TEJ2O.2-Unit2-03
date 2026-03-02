"""
Created by: Ashlyn
Created on: Feb 2026
This module will solve basic math
"""

from microbit import *

display.clear()
sleep(1)

display.scroll("A rectangle has dimensions 5 cm & 3 cm")
display.scroll("The perimeter would be" + 2 * (5 + 3) + " cm")
display.scroll("The area would be" + (5 * 3) + " cm^2")
