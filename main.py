# Импорт библиотек
import managers.managers as managers
import numpy as np

# Начальные параметры
x0 = 7
y0 = 5
r0 = 0.2
r1 = 0.4
r2 = 0.6
r3 = 0.8
r4 = 1
n = 20
h_parts = 1

time = 1
h = 0.01

#time = 0.5
#h = 0.1


# Преобразованная таблица Бутчера
a = np.array([
    [0, 0, 0],  # a0
    [0, 0, 0],  # a1
    [0, 1/2, 0],  # a2
])
b = np.array([0, 0, 1])  #нижняя строка
c = np.array([0, 0, 1/2])  #левый столбец


# Создаём материальное тело и двигаем его
body = managers.cr_mat_body(x0, y0, r0, r1, r2, r3, r4, n)
move = managers.move_mat_body(time, h, body, a, b, c)

# Рисуем траекторию движения тела
managers.plot_trajectory(body, move)

# Составляем поля скоростей и выводим графики
vf = managers.move_through_space(1, 0.1)
managers.plot_vel_fields(vf)