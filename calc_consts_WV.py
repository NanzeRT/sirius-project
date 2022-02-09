#! /usr/bin/python

n = int(input('Count of blocks: '))
R2 = float(input('Cons resist: '))
R1 = float(input('Line segment resist: '))

R1on2 = R1 / R2

v = 1
w = 1

for _ in range(n-1):
    w += v * R1on2
    v += w

print(f'V: {v}\nW: {w}')
