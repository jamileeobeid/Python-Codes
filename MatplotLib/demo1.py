import matplotlib.pyplot as plt
import numpy as np

xpoints = np.array([1,2,3,4,5])
ypoints = np.array([1,50,100,150,200])

plt.plot(xpoints, ypoints, marker = 'o', ms = 10, mec = 'red', mfc = 'black’)
plt.show()

# marker option specifies marker shape
# ms option specifies marker size
# mec option specifies marker edge color
# mfc option specifies marker face color
