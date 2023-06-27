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

    # class cardiopulmonary_endurance(Muscle): # סיבולת לב-ריאה
    def running(self):
        pass
    def cycling(self):
        pass

    # class chest(Muscle):#  חזה
    def bench_press(self):
        pass
    def push_ups(self):
        pass
    def chest_flyes(self):
        pass
    def dumbbell_press(self):
        pass

    # class back(Muscle): #גב
    def pull_ups(self):
        pass
    def rows(self):
        pass
    def lat_pulldowns(self):
        pass

    # class Shoulders(Muscle):  # כתפיים
    def shoulder_press(self):
        pass
    def lateral_raises(self):
        pass
    def front_raises(self):
        pass

    # class Biceps(Muscle): # יד קדמית
    def bicep_curls(self):
        pass
    def hammer_curls(self):
        pass

    # class Triceps(Muscle):  #  יד אחורית
    def Tricep_dips(self):
        pass
    def tricep_pushdowns(self):
        pass

    # class Quadriceps(Muscle):  #  4 ראשי
    def squats(self):
        pass
    def lunges(self):
        pass
    def leg_press(self):
        pass

    # class Hamstrings(Muscle):  # ירכיים
    def deadlifts(self):
        pass
    def hamstring_curls(self):
        pass

    # class Calves(Muscle): # תאומים
    def Calf_raises(self):
        pass

    # class Abdominals(Muscle):# בטן
    def planks(self):
        pass
    def sit_ups(self):
        pass
    def Russian_twists(self):
        pass

    def getvalue(self):
        return [self.points, self.date, self.rast_time]

# Retrieve all classes that inherit from BaseClass
subclasses = Muscle.__subclasses__()
# Create instances of each subclass
# muscle_subclasses = [subclass() for subclass in subclasses]
# print(muscle_subclasses)