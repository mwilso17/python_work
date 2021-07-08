# Mike Wilson 8 July 2021
# A simple test of Matplotlib

import matplotlib.pyplot as plt

squares = [1, 4, 9, 16, 25]

fig, ax = plt.subplots()
ax.plot(squares)

plt.show()