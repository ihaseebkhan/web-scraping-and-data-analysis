from matplotlib import pyplot as plt
from matplotlib import style
import numpy as np

style.use('ggplot')

#Draw a graph to show relation between Total number of ratings & Rating score.

plt.figure(1)
x,y = np.genfromtxt('IMDB.csv', delimiter=',', unpack=True, skip_header=1, usecols=(5, 3))
plt.plot(x,y)
plt.title('Relation between Total number of ratings & Rating score')
plt.xlabel('Total number of ratings')
plt.ylabel('Rating Score')

#Draw a graph to show relation between Budget & Rating Score.

plt.figure(2)
x,y = np.genfromtxt('IMDB.csv', delimiter=',', unpack=True, skip_header=1, usecols=(0, 3),dtype=(str, str))
plt.plot(x,y)
plt.title('Relation between Budget & Rating score')
plt.xlabel('Budget')
plt.ylabel('Rating Score')

plt.show()