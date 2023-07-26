#Machine Learning
#Standard Deviation
import random

import numpy
speed = [86,87,88,86,87,85,86]
x = numpy.std(speed)
print(x)

#percentile
import numpy as np

array = [1,2,4,5,6,7,8,12,13,14,23,24,26,26,70,78,80]

x = numpy.percentile(array, 75)
print(x)

#Data Distribution
import numpy as np

array = [1,2,3,4,5,7,8,9,12,13,14,15,16,17,23,24,25,26,29]

x = numpy.random.uniform(array)

print(x)

#Normal Data Distribution
import numpy
import matplotlib.pyplot as plt

x = numpy.random.normal(5.0, 1.0, 100000)

plt.hist(x, 100)
plt.show()

#Scatter Plot
import matplotlib.pyplot as plt

x = [5,7,8,7,2,17,2,9,4,11,12,9,6]
y = [99,86,87,88,111,86,103,87,94,78,77,85,86]

plt.scatter(x, y)
plt.show()

import matplotlib.pyplot as plt
import numpy as np

x = numpy.random.normal(5.0, 1.0, 1000)
y = numpy.random.normal(10.0, 2.0, 1000)

plt.scatter(x,y)
plt.show()

