# Требуется вывести все целые степени двойки (т.е. числа
# вида 2k), не превосходящие числа N.

n = int(input('введите число'))
p = 1

while p <= n:
    print(p, end=' ')
    p *=2