# Импорт модуля (модели) и библиотек.
import models.models as model
import matplotlib.pyplot as plotlib
import numpy as np


# Задаём V1 и V2
def fx(t, x):
    return - np.exp(t) * x


def fy(t, y):
    return np.exp(t) * y


# Создаем материальное тело
def cr_mat_body(x0, y0, r, n):
    t = 0
    m = 0
    mat_points = []

    # Переходим в полярные координаты
    theta = np.linspace(0, np.pi / 2, n)

    def get_crd(r):
        return x0 + r * np.cos(theta), y0 + r * np.sin(theta)

    xr, yr = get_crd(r)

    # Добавляем материальноые точки
    def add_mpoints(x, y):
        mat_points.append(model.MatPoint(m, x, y, fx(t, x), fy(t, y), x, y, t))

    for i in range(len(xr)):        # range - переход на следующую итерацию цикла до точки (xr,yr)
        add_mpoints(xr[i], yr[i])

    mat_body = model.MatBody(mat_points)
    return mat_body


# Вводим метод Рунге-Кутты (явный)
def runge_method(x0, h, n, func, a, b, c):    # h-величина шага сетки, a,b,c - эл-ты таблицы Бутчера
    xt = [x0]
    t = 0       # Сумма шагов интегрирования за все итерации
    for i in range(n):
        xn = xt[i]
        k1 = func(t, xn)    # 1я стадия
        k2 = func(t + c[2] * h, xn + a[2, 1] * h * k1)  # 2я стадия
        xt.append(xn + h * (k1 * b[1] + k2 * b[2]))     # по общей формуле
        t += h
    return xt


# Действуем на тело
def move_mat_body(time, h, mb, a, b, c):
    point_trajectories = []
    for i in range(len(mb.mat_points)):
        x0 = mb.mat_points[i].x0        # Обращение к координате х0 i-той мат. точки матераиоьного тела
        y0 = mb.mat_points[i].y0
        n = int(time / h) + 1
        xt = runge_method(x0, h, n, fx, a, b, c)
        yt = runge_method(y0, h, n, fy, a, b, c)

        point_trajectories.append(model.PointTrajectory(mb.mat_points[i], xt, yt))
    body_trajectory = model.BodyTrajectory(point_trajectories, mb)
    return body_trajectory


# Строим график траектории движения тела
def plot_trajectory(mb, tr):
    for i in range(len(mb.mat_points)):
        plotlib.plot(mb.mat_points[i].coord_x, mb.mat_points[i].coord_y, 'r.')
    for i in range(len(mb.mat_points)):
        plotlib.plot(tr.point_trajectories[i].x, tr.point_trajectories[i].y, 'b', linewidth=0.5)
    for i in range(len(mb.mat_points)):
        time = len(tr.point_trajectories[i].x) - 1
        plotlib.plot(tr.point_trajectories[i].x[time], tr.point_trajectories[i].y[time], 'g.')
    plotlib.axis('equal')
    plotlib.grid()
    plotlib.show()
    plotlib.savefig('assets/plot_trajectory.svg', format='svg', dpi=1200)


