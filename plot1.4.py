#! /usr/bin/python3
import matplotlib.pyplot as plt

fig, ax = plt.subplots()

yaxU = []
yaxP = []
xax = []

om_per_m = .027 / 154
max_cons_in_one_house = 15000

step = .5
bound = 500

R = om_per_m * step

for cons_in_one_house in range(0, max_cons_in_one_house + 1):
    I = 0
    U = 218
    add_power_per_m = cons_in_one_house / 5 / 3
    dP = add_power_per_m * step * 2
    
    x = 0
    while x <= bound:
        # Q = I ** 2 * R / 2
        U += I * R
        I += dP / U
        x += step
    xax += [cons_in_one_house / 1000]
    yaxU += [U]
    yaxP += [(I * U / 2 - add_power_per_m * bound) / 1000]

ax.set_xlabel('среднее потребление в одном доме (кВт)')
ax.plot(xax, yaxU, label='Напряжение на трансформаторе (В)')
ax.plot(xax, yaxP, label='Энергопотери (кВт)')
ax.annotate(f'{yaxU[0]:.1f}В', (xax[0], yaxU[0]-10))
ax.annotate(f'{yaxP[0]:.1f}кВт', (xax[0], yaxP[0]))

ax.annotate(f'{yaxU[len(xax) * 2 // 15]:.1f}В', (xax[len(xax) * 2 // 15]-.8, yaxU[len(xax) * 2 // 15]+5))
ax.annotate(f'{yaxP[len(xax) * 2 // 15]:.1f}кВт', (xax[len(xax) * 2 // 15]-.8, yaxP[len(xax) * 2 // 15]+5))

ax.annotate(f'{yaxU[-1]:.1f}В', (xax[-1]-1.8, yaxU[-1]+.1))
ax.annotate(f'{yaxP[-1]:.1f}кВт', (xax[-1]-1.8, yaxP[-1]))
ax.grid()
ax.legend()
plt.show()
