from astropy.io import fits
import matplotlib.pyplot as plt

file = fits.open('~/Downloads/v523cas60s-001(1).fit')
tabl = file[0].data

x_c = 1091
y_c = 1036
r = 10
X = []
Y = []
V1 = []
V2 = []
for i in range(x_c - r, x_c + r + 1):
    X.append(i)
    V1.append(tabl[y_c][i])

for i in range(y_c - r, y_c + r + 1):
    Y.append(i)
    V2.append(tabl[i][x_c])

plt.figure()
plt.subplot(1, 2, 1)
plt.plot(X, V1, color = 'orange')
plt.xlabel('X')
plt.ylabel('Value')

plt.subplot(1, 2, 2)
plt.plot(Y, V2)
plt.xlabel('Y')
plt.ylabel('Value')

plt.subplots_adjust(wspace = 0.38)
plt.show()