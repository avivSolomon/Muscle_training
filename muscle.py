from datetime import datetime

class Muscle():

    def __init__(self, points=0, date=0, rast_time=0):
        self.points = points
        self.date = date
        self.rast_time = rast_time

    def update_points(self, points, date, rast_time):
        self.points = points
        self.date = date
        self.rast_time = rast_time

