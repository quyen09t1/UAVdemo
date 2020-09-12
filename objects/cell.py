from objects.vector import Position

# Unit is meter


class BaseStation:
    def __init__(self, p=Position(500, 500, 0), h=20):
        self.position = p
        self.height = h


class Cell:
    def __init__(self, position=Position(500, 500, 0), r=500, bs=BaseStation()):
        self.centerPoint = position
        self.r = r
        self.bs = bs

    def getR(self):
        return self.r

    def setR(self, r):
        self.r = r

    def getBaseStation(self):
        return self.bs

    def setBaseStation(self, bs):
        self.bs = bs

    def getCenterPoint(self):
        return self.centerPoint
