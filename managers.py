# Импорт модуля (модели) и библиотек.
import models.models as model
import matplotlib.pyplot as plotlib
import numpy as np

# Задаём V1 и V2
def f_x(t, x):
    return - np.exp(t) * x


def f_y(t, y):
    return np.exp(t) * y


# Создаем материальное тело
def cr_material_body(x0, y0, r, n):
    t = 0
    m = 0
    material_points = []

    # Переходим в полярные координаты
    theta = np.linspace(0, np.pi / 2, n)

    def get_crd(r):
        return x0 + r * np.cos(theta), y0 + r * np.sin(theta)

    xr, yr = get_crd(r)

    # Добавляем материальноые точки
    def add_mpoints(x, y):
        material_points.append(model.MaterialPoint(m, x, y, f_x(t, x), f_y(t, y), x, y, t))

    for i in range(len(xr)): # range - переход на следующую итерацию цикла до точки (xr,yr)
        add_mpoints(xr[i], yr[i])

    material_body = model.MaterialBody(material_points)
    return material_body

# Вводим метод Рунге-Кутты (явный)
def runge_method(x0, h, n, func, a, b, c):    # h-величина шага сетки, a,b,c - эл-ты таблицы Бутчера
    xt = [x0]
    t = 0
    for i in range(n):
        xn = xt[i]
        k1 = func(t, xn)    # 1я стадия
        k2 = func(t + c[2] * h, xn + a[2, 1] * h * k1)  # 2я стадия
        xt.append(xn + h * (k1 * b[1] + k2 * b[2]))     # по общей формуле
        t += h
    return xt