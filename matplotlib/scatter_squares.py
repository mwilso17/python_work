# Mike Wilson 8 July 2021
# Test of different parts of matplotlib.

import matplotlib.pyplot as plt

plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.scatter(2, 4)

plt.show()