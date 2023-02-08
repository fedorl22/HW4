# Задача FOOTBALL необязательная. Напишите программу, которая принимает на стандартный вход 
# список игр футбольных команд с результатом матча и выводит на стандартный вывод сводную таблицу 
# результатов всех матчей.

# За победу команде начисляется 3 очка, за поражение — 0, за ничью — 1.

# Формат ввода следующий:
# В первой строке указано целое число nn — количество завершенных игр.
# После этого идет nn строк, в которых записаны результаты игры в следующем формате:
# Перваякоманда;Забитопервойкомандой;Втораякоманда;Забитовторойкомандой

# Вывод программы необходимо оформить следующим образом:
# Команда:Всегоигр Побед Ничьих Поражений Всегоочков

# Конкретный пример ввода-вывода приведён ниже.

# Порядок вывода команд произвольный.

# Sample Input:

# 3
# Спартак;9;Зенит;10
# Локомотив;12;Зенит;3
# Спартак;8;Локомотив;15
# Sample Output:

# Спартак:2 0 0 2 0
# Зенит:2 1 0 1 3
# Локомотив:2 2 0 0 6


import itertools
nn = int(input('Введите количество сыграных игр:'))
x_lst = [input('Перваякоманда;Забитопервойкомандой;Втораякоманда;Забитовторойкомандой: ')
          .split(';') for x in range(nn)]
print(x_lst)
vs = [(x[0], x[2]) for x in x_lst]
clubs = set(itertools.chain.from_iterable(vs))
print(clubs)
result = {club:[0, 0, 0, 0, 0] for club in clubs}
print(result)
for k1, g1, k2, g2 in x_lst:
    result[k1][0] += 1
    result[k2][0] += 1
    if int(g1) > int(g2):
        result[k1][1] += 1
        result[k1][4] += 3
        result[k2][3] += 1
    elif int(g1) < int(g2):
        result[k2][1] += 1
        result[k2][4] += 3
        result[k1][3] += 1
    elif int(g1) == int(g2):
        result[k1][2] += 1
        result[k1][4] += 1
        result[k2][2] += 1
        result[k2][4] += 1
for club in clubs:
    print('{}:{}'.format(club, ' '.join(map(str, result[club]))))
