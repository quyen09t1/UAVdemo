from objects.vector import Position, Vector


class User:
    def __init__(self, p=Position(0, 0, 0), v=0, d=Vector(0, 0, 0)):
        self.position = p
        self.velocity = v
        self.direction = d

    def getPosition(self):
        return self.position

    def setPosition(self, p):
        self.position = p

    def getVelocity(self):
        return self.velocity

    def setVelocity(self, v):
        self.velocity = v

    def getDirection(self):
        return self.direction

    def setDirection(self, d):
        self.direction = d


class UAV:
    def __init__(self, p=Position(0, 0, 0), v=0, d=Vector(0, 0, 0)):
        self.position = p
        self.velocity = v
        self.direction = d

    def getPosition(self):
        return self.position

    def setPosition(self, p):
        self.position = p

    def getVelocity(self):
        return self.velocity

    def setVelocity(self, v):
        self.velocity = v

    def getDirection(self):
        return self.direction

    def setDirection(self, d):
        self.direction = d
