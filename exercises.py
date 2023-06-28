from users import User
from gym_manager import GymManager
class Exercise:
    def __init__(self, user_id):
        self.user_id = user_id

    def getMuscle(self, muscle_name):
        cur_muscle = GymManager.get_user(self.user_id).get_muscle(muscle_name)
        return cur_muscle, cur_muscle.get_points()



    # class cardiopulmonary_endurance(Muscle): # סיבולת לב-ריאה
    def running(self, points, train=True):
        for mus in User.muscle_list:
            cur_muscle, cur_point = Exercise.getMuscle(self.user_id, mus)
            if mus in ['cardiopulmonary_endurance', 'triceps', 'quadriceps',
                       'hamstrings', 'calves']:
                cur_muscle.update_points(cur_point + points)
            else:
                cur_muscle.update_points(cur_point + 1)

    def cycling(self, points):
        for mus in User.muscle_list:
            cur_muscle, cur_point = Exercise.getMuscle(self.user_id, mus)
            if mus in ['cardiopulmonary_endurance', 'triceps', 'quadriceps',
                       'hamstrings', 'calves']:
                cur_muscle.update_points(cur_point + points)
            else:
                cur_muscle.update_points(cur_point + 1)

    def swimming(self, points):
        for mus in User.muscle_list:
            cur_muscle, cur_point = Exercise.getMuscle(self.user_id, mus)
            if mus not in ['cardiopulmonary_endurance', 'triceps', 'quadriceps',
                           'hamstrings', 'calves']:
                cur_muscle.update_points(cur_point + points)
            else:
                cur_muscle.update_points(cur_point + 1)

    # class chest(Muscle):#  חזה
    def bench_press(self, points):
        cur_muscle, cur_point = Exercise.getMuscle(self.user_id, 'chest')
        cur_muscle.update_points(cur_point + points)

    def push_ups(self, points):
        cur_muscle, cur_point = Exercise.getMuscle(self.user_id, 'chest')
        cur_muscle.update_points(cur_point + points)

    def chest_flyes(self, points):
        cur_muscle, cur_point = Exercise.getMuscle(self.user_id, 'chest')
        cur_muscle.update_points(cur_point + points)

    def dumbbell_press(self, points):
        cur_muscle, cur_point = Exercise.getMuscle(self.user_id, 'chest')
        cur_muscle.update_points(cur_point + points)

    # class back(Muscle): #גב

    def pull_ups(self, points):
        cur_muscle, cur_point = Exercise.getMuscle(self.user_id, 'back')
        cur_muscle.update_points(cur_point + points)

    def rows(self, points):
        cur_muscle, cur_point = Exercise.getMuscle(self.user_id, 'back')
        cur_muscle.update_points(cur_point + points)
    def lat_pulldowns(self, points):
        cur_muscle, cur_point = Exercise.getMuscle(self.user_id, 'back')
        cur_muscle.update_points(cur_point + points)

     # class Shoulders(Muscle):  # כתפיים
    def shoulder_press(self, points):
        cur_muscle, cur_point = Exercise.getMuscle(self.user_id, 'shoulders')
        cur_muscle.update_points(cur_point + points)

    def lateral_raises(self, points):
        cur_muscle, cur_point = Exercise.getMuscle(self.user_id, 'shoulders')
        cur_muscle.update_points(cur_point + points)

    def front_raises(self, points):
        cur_muscle, cur_point = Exercise.getMuscle(self.user_id, 'shoulders')
        cur_muscle.update_points(cur_point + points)

    # class Biceps(Muscle): # יד קדמית
    def bicep_curls(self, points):
        cur_muscle, cur_point = Exercise.getMuscle(self.user_id, 'biceps')
        cur_muscle.update_points(cur_point + points)

    def hammer_curls(self, points):
        cur_muscle, cur_point = Exercise.getMuscle(self.user_id, 'biceps')
        cur_muscle.update_points(cur_point + points)

    # class Triceps(Muscle):  #  יד אחורית
    def tricep_dips(self, points):
        cur_muscle, cur_point = Exercise.getMuscle(self.user_id, 'triceps')
        cur_muscle.update_points(cur_point + points)

    def tricep_pushdowns(self, points):
        cur_muscle, cur_point = Exercise.getMuscle(self.user_id, 'triceps')
        cur_muscle.update_points(cur_point + points)

    # class Quadriceps(Muscle):  #  4 ראשי
    def squats(self, points):
        cur_muscle, cur_point = Exercise.getMuscle(self.user_id, 'quadriceps')
        cur_muscle.update_points(cur_point + points)

    def lunges(self, points):
        cur_muscle, cur_point = Exercise.getMuscle(self.user_id, 'quadriceps')
        cur_muscle.update_points(cur_point + points)

    def leg_press(self, points):
        cur_muscle, cur_point = Exercise.getMuscle(self.user_id, 'quadriceps')
        cur_muscle.update_points(cur_point + points)

    # class Hamstrings(Muscle):  # ירכיים
    def deadlifts(self, points):
        cur_muscle, cur_point = Exercise.getMuscle(self.user_id, 'hamstrings')
        cur_muscle.update_points(cur_point + points)

    def hamstring_curls(self, points):
        cur_muscle, cur_point = Exercise.getMuscle(self.user_id, 'hamstrings')
        cur_muscle.update_points(cur_point + points)

    # class Calves(Muscle): # תאומים
    def Calf_raises(self, points):
        cur_muscle, cur_point = Exercise.getMuscle(self.user_id, 'calves')
        cur_muscle.update_points(cur_point + points)


    # class Abdominals(Muscle):# בטן
    def planks(self, points):
        cur_muscle, cur_point = Exercise.getMuscle(self.user_id, 'abdominals')
        cur_muscle.update_points(cur_point + points)
        cur_muscle, cur_point = Exercise.getMuscle(self.user_id, 'back')
        cur_muscle.update_points(cur_point + points)

    def sit_ups(self, points):
        cur_muscle, cur_point = Exercise.getMuscle(self.user_id, 'abdominals')
        cur_muscle.update_points(cur_point + points)

    def Russian_twists(self, points):
        cur_muscle, cur_point = Exercise.getMuscle(self.user_id, 'abdominals')
        cur_muscle.update_points(cur_point + points)

