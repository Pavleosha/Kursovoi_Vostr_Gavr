class MaterialPoint:
    def __init__(self, i, crd_x, crd_y, vel_x, vel_y, x0, y0, t):
        self.i = i
        self.crd_x = crd_x
        self.crd_y = crd_y
        self.vel_x = vel_x
        self.vel_y = vel_y
        self.x0 = x0
        self.y0 = y0
        self.t = t


class MaterialBody:
    def __init__(self, material_points):
        self.material_points = material_points


class PointTrajectory:
    def __init__(self, material_point, x, y):
        self.material_point = material_point
        self.x = x
        self.y = y


class BodyTrajectory:
    def __init__(self, point_trajectories, material_body):
        self.point_trajectories = point_trajectories
        self.material_body = material_body


class SpacePoint:
    def __init__(self, i, crd_x, crd_y, vel_x, vel_y, t):
        self.i = i
        self.crd_x = crd_x
        self.crd_y = crd_y
        self.vel_x = vel_x
        self.vel_y = vel_y
        self.t = t


class SpaceGrid:
    def __init__(self, space_points):
        self.space_points = space_points
