# : На столе лежат n монеток. Некоторые из них лежат вверх
# решкой, а некоторые – гербом. Определите минимальное число
# монеток, которые нужно перевернуть, чтобы все монетки были
# повернуты вверх одной и той же стороной. Выведите минимальное
# количество монет, которые нужно перевернуть.

import random
n = int(input('введите количество монет: '))
orel = 0
reshka = 0
#side = int(input('введите 0 или 1: '))
for i in range(n):
    side = random.randint(0, 2)
    if side == 1:
        orel += 1
    else:
        reshka +=1    
if orel < reshka:
    print(f'орел: {orel}' )
elif orel > reshka:
    print(f'решка: {reshka}')
else:
    print(f'количество сторон равное: {orel}')     
