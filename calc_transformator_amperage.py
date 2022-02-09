#! /usr/bin/python3

U1 = float(input('Введите напряжение накопителя (В) (по ум. 220) -> ') or 220)
U = float(input('Введите напряжение трансформатора (В) (по ум. 230) -> ') or 230)

R1 = .00265
R2 = 12.1
num_of_segments = 33

X2k0 = 0
X2k1 = 1

R1overR2 = R1/R2

for _ in range(num_of_segments-1):
    X2k0 = X2k1 + X2k0
    X2k1 = X2k0 * R1overR2 + X2k1
X2k0 = X2k1 + X2k0

I = (- U1 * R2 + U * X2k0 * R1 + U * R2 * X2k1) / (X2k0 * R1 * R2)

print(f'Сила тока трансформатора: {I} А\nМощность выдаваемого тока: {I * U / 2 / 1000} кВт')
