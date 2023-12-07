import astropy.io.fits as asp

start = asp.open('~/Downloads/v523cas60s-001(1).fit')
info = start[0].data
start.close()

x_c = int(input('Введите координату x центра звезды: '))
y_c = int(input('Введите координату y центра звезды: '))
R_star = int(input('Введите радиус звезды: '))
r_ring = int(input('Введите радиус кольца: '))
Texp = 60
E = 0     # энергия от звезды
E_r = 0   # энергия от кольца
pix_star = 0
pix_ring = 0

for x in range(x_c - R_star, x_c + R_star + 1):
    for y in range(y_c - R_star, y_c + R_star + 1):
        if (x - x_c)**2 + (y - y_c)**2 <= R_star**2:
            E = E + info[y][x]
            pix_star = pix_star + 1
print('E =', E)

for x1 in range(x_c - r_ring, x_c + r_ring + 1):
    for y1 in range(y_c - r_ring, y_c + r_ring + 1):
        if R_star**2 < (x1 - x_c)**2 + (y1 - y_c)**2 and (x1 - x_c)**2 + (y1 - y_c)**2 <= r_ring**2:
            E_r = E_r + info[y1][x1]
            pix_ring = pix_ring + 1
print('E_r =', E_r)
print('pix_star = ', pix_star, 'pix_ring =', pix_ring)

S = E / Texp    # энергия от звезды за 1 секунду
E_sr = E_r / (Texp * pix_ring)  # средний фон на 1 пиксель
N_f = E_sr * pix_star  # фон на звезде
I = S - N_f
print('S =', S, 'E_sr =', E_sr, 'N_f =', N_f)
print('I =', I)