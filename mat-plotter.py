import numpy as np 
import matplotlib.pyplot as plt
import sys

infile = sys.argv[1] 	# takes in .mat files (matrices)
filename = infile.split('.')[0]

with open(infile) as f:
	mtx = []
	for line in f.readlines():
		ls = line.split(None)
		mtx.append(ls)	

mat = np.array(mtx, dtype=float)

fig = plt.figure()
ax = fig.add_subplot(111)
ax.set_title('colormap')
plt.imshow(mat, cmap='Blues')
ax.set_aspect('equal')

plt.colorbar()
plt.savefig(filename+'-plotted', dpi=300)
plt.show()
