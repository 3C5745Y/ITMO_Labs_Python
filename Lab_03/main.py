import math
help(math)
print(dir(math))

import statistics
help(statistics)
print(dir(statistics))

list = [13,23,38,44,155,68,72,81,90,100]
print(list)
print("Sum of the numbers in list: ", math.fsum(list))
print("Average number in list: ", statistics.mean(list))
print("Median: ", statistics.median(list))
print("Standard Deviation: ", statistics.stdev(list))


import random as ran, numpy as np
print("Random integer between 1 and 100: ", ran.randint(1,100))
