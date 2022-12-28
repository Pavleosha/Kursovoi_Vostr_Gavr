# Импорт модуля (модели) и библиотек.
import models.models as model
import matplotlib.pyplot as plotlib
import numpy as np

# Задаём V1 и V2
def f_x(t, x):
    return - np.exp(t) * x


def f_y(t, y):
    return np.exp(t) * y