#! /usr/bin/python3
import matplotlib.pyplot as plt

fig, ax = plt.subplots()



yaxU1 = []
yaxU2 = []
yaxI = [] # сила на ЛЭП
yaxPl = []
yaxPc = []
xax = []

R1 = .00265
R2 = 12.1
Ut = 230 # transformator
Uc = 220 # cell
Ic = 193.5
Rc = Uc / Ic
line_lenght = 500
num_of_segments = 33
segment_len = line_lenght / num_of_segments

xax += [line_lenght]
yaxU2 += [Uc]
yaxU1 += [yaxU2[0] * R1 / R2 - Uc * R1 / Rc]
yaxI += [yaxU1[0] / R1]
yaxPl += [yaxI[0] * yaxU1[0] / 2]
yaxPc += [yaxU2[0] ** 2 / R2 / 2 / 10]

for i in range(1, num_of_segments):
    xax += [line_lenght - segment_len * i]
    yaxU2 += [yaxU2[i - 1] + yaxU1[i - 1]]
    yaxU1 += [yaxU2[i] * R1 / R2 + yaxU1[i - 1]]
    yaxI += [yaxU1[i] / R1]
    yaxPl += [yaxI[i] * yaxU1[i] / 2]
    yaxPc += [yaxU2[i] ** 2 / R2 / 2 / 10]

i += 1
xax += [0]
yaxU2 += [yaxU2[i - 1] + yaxU1[i - 1]]
yaxPc += [yaxU2[i] ** 2 / R2 / 2 / 10]

yaxU1 = list(j * 100 for j in yaxU1)

ax.set_xlabel('Расстояние от трансформатора (м)')
ax.plot(xax[:-1], yaxI, label='Сила тока на сегменте ЛЭП (А)')
ax.plot(xax, yaxU2, label=f'Напряжение у потребителя (В) Min: {min(yaxU2):.1f} В Max: {max(yaxU2):.1f} В')
ax.plot(xax[:-1], yaxU1, label='Напряжение сегмента ЛЭП (мВ*10)', ls='--')
ax.plot(xax[:-1], yaxPl, label=f'Энергопотери на сегменте ЛЭП (Вт) Sum: {sum(yaxPl) / 1000:.1f} кВт', ls='-.')
ax.plot(xax, yaxPc, label='Потребляемая мощность потребителем (кВт*10)', ls=':')

ax.grid()
ax.legend()
plt.show()
