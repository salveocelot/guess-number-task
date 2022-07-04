print('test1')
   


from re import M
import numpy as np
number=int(input('Введите число: '))
count=0
predict_number = 50
max=100
min=0

while True:
    count += 1
    if predict_number < number:
        min=predict_number
        predict_number=(max+min)//2

    elif predict_number > number:
        max=predict_number
        predict_number=(max+min)//2
        
    else:
        print(f"Вы угадали число! Это число = {number}, за {count} попыток")
        break # конец игры, выход из цикла


