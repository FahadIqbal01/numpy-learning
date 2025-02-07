# Matplotlib (pyplot) - seaborn
# Seaborn is a library that uses matplotlib underneath to plot graph i.e, pyplot.

import matplotlib.pyplot as plt
import seaborn as sb
sb.displot(data=[0, 1, 2, 3, 4, 5])
plt.show()

# Plotting a distplot without histogram
sb.displot(data= [0, 1, 2, 3, 4, 5], kind= 'hist')
plt.show()