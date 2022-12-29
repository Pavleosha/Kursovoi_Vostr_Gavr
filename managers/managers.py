import models as model      # Подключаем моудль "модели"
import matplotlib.pyplot as plotlib     # подключаем библиотеку для создания графиков
import numpy as np      # подключаем библиотеку для работы с математическими функциями


# Задаём функции V1 и V2
def fx(t, x):       # Функция V1
    return -np.exp(t) * x


def fy(t, y):       # Функция V2
    return np.exp(t) * y


# Создаем материальное тело (круг)
def cr_mat_body(x0, y0, r0, r1, r2, r3, r4, n):
    t = 0       # initial time of mpoints
    m = 0       # initial position of mpoints
    mat_points = []     # create empty array of mpoints

    # Перейдем в полярные координаты
    phi = np.linspace(0, 2*np.pi, n)      # unit angle of rotation

    def get_crd(r):
        return x0 + r * np.cos(phi), y0 + r * np.sin(phi)       # Непосредсвтенный переход

    xr0, yr0 = get_crd(r0)      # create arc of circle
    xr1, yr1 = get_crd(r1)
    xr2, yr2 = get_crd(r2)
    xr3, yr3 = get_crd(r3)
    xr4, yr4 = get_crd(r4)

    # Добавляем материальноые точки
    def add_mpoints(x, y):
        # defining the array class
        mat_points.append(model.MatPoint(m, x, y, fx(t, x), fy(t, y), x, y, t))

    for i in range(len(xr4)):
        # filling the array with mpoints
        add_mpoints(x0, y0)
        add_mpoints(xr0[i], yr0[i])
        add_mpoints(xr1[i], yr1[i])
        add_mpoints(xr2[i], yr2[i])
        add_mpoints(xr3[i], yr3[i])
        add_mpoints(xr4[i], yr4[i])

    mat_body = model.MatBody(mat_points)        # we combine the points into a body
    return mat_body


# We introduce the explicit Runge-Kutta method
def runge_method(x0, h, n, func, a, b, c):    # h - integration step, a,b,c - elements Butcher's table
    xt = [x0]
    t = 0       # sum of iteration steps
    for i in range(n):
        xn = xt[i]
        k1 = func(t, xn)    # 1st stage
        k2 = func(t + c[2] * h, xn + a[2, 1] * h * k1)  # 2nd stage
        xt.append(xn + h * (k1 * b[1] + k2 * b[2]))     # general formula
        t += h
    return xt


# Действуем на тело
def move_mat_body(time, h, mb, a, b, c):
    point_trajectories = []     # create empty array
    for i in range(len(mb.mat_points)):
        x0 = mb.mat_points[i].x0        # Обращение к координате х0 i-той мат. точки матераиоьного тела
        y0 = mb.mat_points[i].y0
        n = int(time / h) + 1
        xt = runge_method(x0, h, n, fx, a, b, c)        # Обращаемся к методу Рунге-Кутты
        yt = runge_method(y0, h, n, fy, a, b, c)

        # filling the array
        point_trajectories.append(model.PointTrajectory(mb.mat_points[i], xt, yt))
    body_trajectory = model.BodyTrajectory(point_trajectories, mb)
    return body_trajectory


# Строим график траектории движения тела
def plot_trajectory(mb, tr):
    for i in range(len(mb.mat_points)):
        plotlib.plot(mb.mat_points[i].crd_x, mb.mat_points[i].crd_y, 'r.')      # make initial circle witch red dots
    for i in range(len(mb.mat_points)):
        # make blue trajectory line with specific length
        plotlib.plot(tr.point_trajectories[i].x, tr.point_trajectories[i].y, 'b', linewidth=0.5)
    for i in range(len(mb.mat_points)):
        # at the ends of the lines we build the green dots of the final figure
        time = len(tr.point_trajectories[i].x) - 1
        plotlib.plot(tr.point_trajectories[i].x[time], tr.point_trajectories[i].y[time], 'g.')
    plotlib.axis('equal')   # make axis
    plotlib.grid()      # make grid
    # plotlib.show()
    plotlib.savefig('plots/plot_trajectory.png', format='png', dpi=1200)        # saving our plots


def move_through_space(time, h):
    t = h
    m = 0
    a = np.linspace(-3, 3, 7)

    x_s, y_s = np.meshgrid(a, a)
    velocity_fields = []

    for n in range(int(time/h)):
        space_points = []
        for i in range(7):
            for j in range(7):
                x = x_s[i, j]
                y = y_s[i, j]
                space_points.append(model.SpacePoint(m, x, y, fx(t, x), fy(t, y), t))
                m += 1
        velocity_fields.append(model.SpaceGrid(space_points))
        t += h
    return velocity_fields


# Строим графики полей скоростей и линий тока
def plot_vel_fields(vf):
    h = vf[0].space_points[0].t
    t = h
    for n in range(len(vf)):
        plotlib.figure(n)
        plotlib.suptitle('t = ' + str(t))
        m = 0
        crd_x = []
        crd_y = []
        vel_x = []
        vel_y = []
        for i in range(7):   # графики полей скоростей
            for j in range(7):
                crd_x.append(vf[n].space_points[m].crd_x)
                crd_y.append(vf[n].space_points[m].crd_y)
                vel_x.append(vf[n].space_points[m].vel_x)
                vel_y.append(vf[n].space_points[m].vel_y)
                m += 1
        plotlib.subplot(1, 2, 1)
        plotlib.quiver(crd_x, crd_y, vel_x, vel_y)
        for p in range(1, 3):   # графики линий тока
            for q in range(1, 3):
                x = np.linspace(0.1, 5.0, 100)
                d = fy(t, 1) / fx(t, 1)
                c = q * (p ** d)
                y = c * (-x ** d)
                plotlib.subplot(1, 2, 2)
                plotlib.axis([-1, 3, -3, 1])
                plotlib.plot(x, y)
        t += h
        # plotlib.show()
        plotlib.savefig('plots/velocity_fields' + str(n) + '.png', format='png', dpi=1200)
