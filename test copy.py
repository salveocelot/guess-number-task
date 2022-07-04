print('test')
   


import numpy as np


def random_predict(number:int=1) -> int:
    count=0
    predict_number = np.random.randint(1, 101) #предполагаемое число
    
    #if predict_number>number:
    #    predict_number=predict_number//2    
    while True:
        count += 1
        if predict_number > number:
            delta=predict_number-predict_number//2
            predict_number=predict_number-delta

        elif predict_number < number:
            delta=(100-predict_number)//2
            predict_number=predict_number+delta

        else:
            #print(f"Вы угадали число! Это число = {number}, за {count} попыток")
            break # конец игры, выход из цикла
    return(count)               
    
def score_game(random_predict) -> int:
    """За какое количество попыток в среднем из 1000 подходов угадывает наш алгоритм

    Args:
        random_predict ([type]): функция угадывания

    Returns:
        int: среднее количество попыток
    """

    count_ls = [] # список для сохранения количества попыток
    np.random.seed(1) # фиксируем сид для воспроизводимости
    random_array = np.random.randint(1, 101, size=(1000)) # загадали список чисел

    for number in random_array:
        count_ls.append(random_predict(number))

    score = int(np.mean(count_ls)) # находим среднее количество попыток

    print(f'Ваш алгоритм угадывает число в среднем за: {score} попыток')
    return(score)

# RUN
score_game(random_predict)