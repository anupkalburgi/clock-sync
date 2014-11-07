import numpy as np
import matplotlib.pyplot as plt

x = []
with open("breeze_logs/CAL_LOG.log") as f:
    lines = f.readlines()
    for line in lines:
    	x.append( float(line.split(" ")[3]) * 100 )

# the histogram of the data
n, bins, patches = plt.hist(x, 84970, normed=0, facecolor='blue', alpha=0.90)

# # # Bins is distribution of values
# print bins
# print n

plt.axis([1.2, 1.7,0, 450])


#plt.text(60, .025, r'$\mu=100,\ \sigma=15$')
plt.xlabel('Drift Rate (mili Seconds)/second')
plt.ylabel('No Records')
plt.title('Histogram of Drift Rate')
plt.grid(True)
plt.show()