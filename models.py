# Определение мат точки
class MatPoint:
    # При определении каждого класса зададим его свойства
    def __init__(self, crd_x, crd_y, vel_x, vel_y, x0, y0, t):
       # self.i = i
        self.crd_x = crd_x
        self.crd_y = crd_y
        self.vel_x = vel_x
        self.vel_y = vel_y
        self.x0 = x0
        self.y0 = y0
        self.t = t


# Определение мат тела
class MatBody:
    def __init__(self, mat_points):
        self.mat_points = mat_points


# Определение траектории точки
class PointTrajectory:

    def __init__(self, mat_point, x, y):
        self.mat_point = mat_point
        self.x = x
        self.y = y


# Определение траектории тела
class BodyTrajectory:
    def __init__(self, point_trajectories, mat_body):
        self.point_trajectories = point_trajectories
        self.mat_body = mat_body


# Определение точки пространства
class SpacePoint:
    def __init__(self, crd_x, crd_y, vel_x, vel_y, t):
        self.crd_x = crd_x
        self.crd_y = crd_y
        self.vel_x = vel_x
        self.vel_y = vel_y
        self.t = t


# Определение сетки
class SpaceGrid:
    def __init__(self, space_points):
        self.space_points = space_points
