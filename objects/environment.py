import random
import math
from objects.vector import Position, Vector
from objects.vehicle import User, UAV

# Unit is meter and second


class Point4Draw:
    def __init__(self, x=[], y=[], z=[]):
        self.x = x
        self.y = y
        self.z = z


class SingleEnv:
    def __init__(self, c, numberOfUser, numberOfUAV, numberOfStep, timeStep):
        self.cell = c
        self.numberOfStep = numberOfStep
        self.timeStep = timeStep
        centerPoint = c.getCenterPoint()

        # Random users
        self.listUser = []
        for i in range(numberOfUser):
            # velocity random from 10 m/s to 30 m/s
            v = random.randint(10, 30)
            p = Position(random.randint(centerPoint.x / 2,
                                        centerPoint.x / 2 + centerPoint.x),
                         random.randint(300, 700),
                         0)
            d = Vector(random.randint(-10, 10),
                       random.randint(-10, 10),
                       0)
            self.listUser.append(User(p, v, d))

        # Random UAVs
        self.listUAV = []
        for i in range(numberOfUAV):
            # velocity random from 10 m/s to 30 m/s
            v = random.randint(10, 30)
            p = Position(random.randint(200, 500),
                         random.randint(200, 500),
                         random.randint(5, 10))
            d = Vector(random.randint(-10, 10),
                       random.randint(-10, 10),
                       random.randint(-3, 3) * 0.01)
            self.listUAV.append(UAV(p, v, d))

    def getUsers(self):
        return self.listUser

    def getUAVs(self):
        return self.listUAV

    def generateUserPoints(self):
        listPoints = []
        for j in range(self.numberOfStep):
            x, y, z = [], [], []
            for item in self.listUser:
                st = item.velocity * j * self.timeStep
                t = math.sqrt(item.direction.x * item.direction.x +
                              item.direction.y * item.direction.y)
                x.append(item.position.x + item.direction.x * st / t)
                y.append(item.position.y + item.direction.y * st / t)
                z.append(0)
            listPoints.append(Point4Draw(x, y, z))
        return listPoints

    def generateUAVPoints(self):
        listPoints = []
        for j in range(self.numberOfStep):
            x, y, z = [], [], []
            for item in self.listUAV:
                st = item.velocity * j * self.timeStep
                t = math.sqrt(item.direction.x * item.direction.x
                              + item.direction.y * item.direction.y
                              + item.direction.z * item.direction.z)
                x.append(item.position.x + item.direction.x * st / t)
                y.append(item.position.y + item.direction.y * st / t)
                z.append(item.position.z + item.direction.z * st / t
                         if (item.position.z + item.direction.z * st / t > 0)
                         else 0)
            listPoints.append(Point4Draw(x, y, z))
        return listPoints
