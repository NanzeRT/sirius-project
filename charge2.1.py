#! /usr/bin/python3
import matplotlib.pyplot as plt

fig, ax = plt.subplots()

yaxP = []
yaxI = []
xax = [] # U

R1 = .00265
R2 = 12.1
U1 = 230
num_of_segments = 33

Ub = 200
Ue = 230
step = .5

X2k0 = 0
X2k1 = 1

R1overR2 = R1/R2

for _ in range(num_of_segments-1):
    X2k0 = X2k1 + X2k0
    X2k1 = X2k0 * R1overR2 + X2k1
X2k0 = X2k1 + X2k0

print(f'Xn = {X2k0}')
print(f'Xn-1 = {X2k1}')

U = Ub
while U <= Ue:
    xax += [U]
    I = (- U1 * R2 + U * X2k0 * R1 + U * R2 * X2k1) / (X2k0 * R1 * R2)
    yaxI += [I]
    yaxP += [U * I / 1000 / 2]
    U += step

ax.set_xlabel('Напряжение накопителя (В)')
ax.plot(xax, yaxP, label='Выдаваемая мощность (кВт)')
ax.plot(xax, yaxI, label='Сила тока (А)')
'''
ax.annotate(f'{yaxU[0]:.1f}В', (xax[0], yaxU[0]+5))
ax.annotate(f'{yaxU[-1]:.1f}В', (xax[-1]-50, yaxU[-1]+5))
ax.annotate(f'{yaxI[0]:.1f}А', (xax[0], yaxI[0]))
ax.annotate(f'{yaxI[-1]:.1f}А', (xax[-1]-50, yaxI[-1]))
'''
ax.grid(True)
ax.legend()
plt.show()
