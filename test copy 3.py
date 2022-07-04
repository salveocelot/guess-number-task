print('test1')
   


import numpy as np
number=int(input('Введите число: '))
count=0
predict_number = np.random.randint(1, 101) #предполагаемое число

while True:
    count += 1
    if predict_number < number:
        delta=predict_number-predict_number//2
        predict_number=predict_number-delta

    elif predict_number > number:
        delta=(100-predict_number)//2
        predict_number=predict_number+delta

    else:
        print(f"Вы угадали число! Это число = {number}, за {count} попыток")
        break # конец игры, выход из цикла


