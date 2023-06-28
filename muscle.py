from datetime import date, timedelta

class Muscle:
    def __init__(self, name, points=0, date=0, rest_time=0):
        self.name = name
        self.points = points
        self.date = date
        self.rest_time = rest_time

    def get_name(self):
        return self.name

    def get_points(self):
        return self.points

    def get_date(self):
        return self.date

    def get_rest_time(self):
        return self.rest_time

    def update_points(self, points, dat=date.today()):
        self.points = points
        self.date = dat
        day_rest = 0 if points<2 else 1 if points<3 else 2
        self.rest_time = self.date + timedelta(days=day_rest)

    def in_rest(self):
        return (self.rest_time - date.today()).days > 0

    def getvalue(self):
        return [self.points, self.date, self.rest_time]

# Retrieve all classes that inherit from BaseClass
subclasses = Muscle.__subclasses__()
# Create instances of each subclass
# muscle_subclasses = [subclass() for subclass in subclasses]
# print(muscle_subclasses)