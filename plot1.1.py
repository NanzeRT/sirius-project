#! /usr/bin/python3
import matplotlib.pyplot as plt

fig, ax = plt.subplots()

yaxU = []
yaxI = []
xax = []

I = 0
U = 220
add_power_per_m = 1000
step = .5
bound = 500
x = 0

dP = add_power_per_m * step * 2

while x <= bound:
    xax += [x]
    yaxU += [U]
    yaxI += [I]
    I += dP / U
    x += step

ax.set_xlabel('расстояние от конца линии (м)')
ax.plot(xax, yaxU, label='Напряжение (В)')
ax.plot(xax, yaxI, label='Сила тока (А)')
ax.annotate(f'{yaxU[0]:.1f}В', (xax[0], yaxU[0]+5))
ax.annotate(f'{yaxU[-1]:.1f}В', (xax[-1]-50, yaxU[-1]+5))
ax.annotate(f'{yaxI[0]:.1f}А', (xax[0], yaxI[0]))
ax.annotate(f'{yaxI[-1]:.1f}А', (xax[-1]-50, yaxI[-1]))
ax.legend()
ax.grid()
plt.show()
