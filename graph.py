import matplotlib.pyplot as plt
f = open('PZ Mon_v_radial.dat', 'r')
r = f.readlines()
start = []
for i in r:
    start.append(i)
del start[0]

str = ''.join(start)
a = str.split('\n')
A = ' '.join(a)
otd = A.split()

X = otd[ : :2]
Y = otd[1: :2]

x = []
y = []
for i in X:
    x_1 = float(i)
    x.append(x_1)
for g in Y:
    y_1 = float(g)
    y.append(y_1)

grph = plt.figure()
plt.scatter(x,y)
plt.xlabel('MJD')
plt.ylabel('Vr')
plt.show()


