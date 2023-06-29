from users import User

class Exercise:
    def __init__(self, gym_manager, user_id):
        self.gym_manager = gym_manager
        self.user_id = user_id

    def get_cur_muscle(self, muscle_name):
        cur_muscle = self.gym_manager.get_user(self.user_id).get_muscle(muscle_name)
        return cur_muscle, cur_muscle.get_points()

    # class cardiopulmonary_endurance(Muscle): # סיבולת לב-ריאה
    def running(self, points, train=True):
        for muscle_name in User.muscle_list:
            cur_muscle, cur_point = self.get_cur_muscle(muscle_name)
            if muscle_name in ['cardiopulmonary_endurance', 'triceps', 'quadriceps',
                               'hamstrings', 'calves']:
                cur_muscle.update_points(cur_point + points)
            else:
                cur_muscle.update_points(cur_point + 1)

    def cycling(self, points):
        for muscle_name in User.muscle_list:
            cur_muscle, cur_point = self.get_cur_muscle(muscle_name)
            if muscle_name in ['cardiopulmonary_endurance', 'triceps', 'quadriceps',
                               'hamstrings', 'calves']:
                cur_muscle.update_points(cur_point + points)
            else:
                cur_muscle.update_points(cur_point + 1)

    def swimming(self, points):
        for muscle_name in User.muscle_list:
            cur_muscle, cur_point = self.get_cur_muscle(muscle_name)
            if muscle_name in ['cardiopulmonary_endurance', 'triceps', 'quadriceps',
                               'hamstrings', 'calves']:
                cur_muscle.update_points(cur_point + points)
            else:
                cur_muscle.update_points(cur_point + 1)

    # class chest(Muscle):#  חזה
    def bench_press(self, points):
        cur_muscle, cur_point = self.get_cur_muscle('chest')
        cur_muscle.update_points(cur_point + points)

    def push_ups(self, points):
        cur_muscle, cur_point = self.get_cur_muscle('chest')
        cur_muscle.update_points(cur_point + points)

    def chest_flyes(self, points):
        cur_muscle, cur_point = self.get_cur_muscle('chest')
        cur_muscle.update_points(cur_point + points)

    def dumbbell_press(self, points):
        cur_muscle, cur_point = self.get_cur_muscle('chest')
        cur_muscle.update_points(cur_point + points)

    # class back(Muscle): #גב

    def pull_ups(self, points):
        cur_muscle, cur_point = self.get_cur_muscle('back')
        cur_muscle.update_points(cur_point + points)

    def rows(self, points):
        cur_muscle, cur_point = self.get_cur_muscle('back')
        cur_muscle.update_points(cur_point + points)

    def lat_pulldowns(self, points):
        cur_muscle, cur_point = self.get_cur_muscle('back')
        cur_muscle.update_points(cur_point + points)

    # class Shoulders(Muscle):  # כתפיים
    def shoulder_press(self, points):
        cur_muscle, cur_point = self.get_cur_muscle('shoulders')
        cur_muscle.update_points(cur_point + points)

    def lateral_raises(self, points):
        cur_muscle, cur_point = self.get_cur_muscle('shoulders')
        cur_muscle.update_points(cur_point + points)

    def front_raises(self, points):
        cur_muscle, cur_point = self.get_cur_muscle('shoulders')
        cur_muscle.update_points(cur_point + points)

    # class Biceps(Muscle): # יד קדמית
    def bicep_curls(self, points):
        cur_muscle, cur_point = self.get_cur_muscle('biceps')
        cur_muscle.update_points(cur_point + points)

    def hammer_curls(self, points):
        cur_muscle, cur_point = self.get_cur_muscle('biceps')
        cur_muscle.update_points(cur_point + points)

    # class Triceps(Muscle):  #  יד אחורית
    def triceps_dips(self, points):
        cur_muscle, cur_point = self.get_cur_muscle('triceps')
        cur_muscle.update_points(cur_point + points)

    def triceps_pushdowns(self, points):
        cur_muscle, cur_point = self.get_cur_muscle('triceps')
        cur_muscle.update_points(cur_point + points)

    # class Quadriceps(Muscle):  #  4 ראשי
    def squats(self, points):
        cur_muscle, cur_point = self.get_cur_muscle('quadriceps')
        cur_muscle.update_points(cur_point + points)

    def lunges(self, points):
        cur_muscle, cur_point = self.get_cur_muscle('quadriceps')
        cur_muscle.update_points(cur_point + points)

    def leg_press(self, points):
        cur_muscle, cur_point = self.get_cur_muscle('quadriceps')
        cur_muscle.update_points(cur_point + points)

    # class Hamstrings(Muscle):  # ירכיים
    def deadlifts(self, points):
        cur_muscle, cur_point = self.get_cur_muscle('hamstrings')
        cur_muscle.update_points(cur_point + points)

    def hamstring_curls(self, points):
        cur_muscle, cur_point = self.get_cur_muscle('hamstrings')
        cur_muscle.update_points(cur_point + points)

    # class Calves(Muscle): # תאומים
    def calf_raises(self, points):
        cur_muscle, cur_point = self.get_cur_muscle('calves')
        cur_muscle.update_points(cur_point + points)

    # class Abdominal(Muscle):# בטן
    def planks(self, points):
        cur_muscle, cur_point = self.get_cur_muscle('abdominal')
        cur_muscle.update_points(cur_point + points)
        cur_muscle, cur_point = self.get_cur_muscle('back')
        cur_muscle.update_points(cur_point + points)

    def sit_ups(self, points):
        cur_muscle, cur_point = self.get_cur_muscle('abdominal')
        cur_muscle.update_points(cur_point + points)

    def russian_twists(self, points):
        cur_muscle, cur_point = self.get_cur_muscle('abdominal')
        cur_muscle.update_points(cur_point + points)

