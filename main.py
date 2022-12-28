# Импорт библиотек
import managers.managers as managers
import numpy as np

# Параметры решателя
x0 = 5
y0 = -10
r = 1
n = 10
h_parts = 1
time = 1
h = 0.0001

# Преобразованная таблица Бутчера
a = np.array([
    [0, 0, 0],  # a0
    [0, 0, 0],  # a1
    [0, 1 / 2, 0],  # a2
])
b = np.array([0, 0, 1])  #нижняя строка
c = np.array([0, 0, 1 / 2])  #левый столбец


# Создаём материальное тело и двигаем его
body = managers.cr_mat_body(x0, y0, r, n)
move = managers.move_mat_body(time, h, body, a, b, c)

# Рисуем траекторию движения тела
managers.plot_trajectory(body, move)

# Составляем поля скоростей и выводим графики
vf = managers.move_through_space(1, 0.1)
managers.plot_vel_fields(vf)