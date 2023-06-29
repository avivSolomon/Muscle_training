from users import User
import sqlite3
from datetime import date
from gym_manager import GymManager


class Exercise:
    def __init__(self, gym_manager, user_id):
        self.gym_manager = gym_manager
        self.user_id = user_id
        self.exercise_name = ''
        self.exercise_date = date.today()
        self.points = 0

    def get_cur_muscle(self, muscle_name):
        cur_user = self.gym_manager.get_user(self.user_id)
        cur_muscle = cur_user.get_muscle(muscle_name)
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
        self.exercise_name = 'running'
        self.points = points
        self.save_exercise_to_database()

    def cycling(self, points):
        for mus in User.muscle_list:
            cur_muscle, cur_point = Exercise.get_cur_muscle(self.user_id, mus)
            if mus in ['cardiopulmonary_endurance', 'triceps', 'quadriceps',
                       'hamstrings', 'calves']:
                cur_muscle.update_points(cur_point + points)
            else:
                cur_muscle.update_points(cur_point + 1)
        self.exercise_name = 'cycling'
        self.points = points
        self.save_exercise_to_database()

    def swimming(self, points):
        for mus in User.muscle_list:
            cur_muscle, cur_point = Exercise.get_cur_muscle(self.user_id, mus)
            if mus not in ['cardiopulmonary_endurance', 'triceps', 'quadriceps',
                           'hamstrings', 'calves']:
                cur_muscle.update_points(cur_point + points)
            else:
                cur_muscle.update_points(cur_point + 1)
        self.exercise_name = 'swimming'
        self.points = points
        self.save_exercise_to_database()

    # class chest(Muscle):#  חזה
    def bench_press(self, points):
        cur_muscle, cur_point = Exercise.get_cur_muscle(self.user_id, 'chest')
        cur_muscle.update_points(cur_point + points)
        self.exercise_name = 'bench_press'
        self.points = points
        self.save_exercise_to_database()

    def push_ups(self, points):
        cur_muscle, cur_point = Exercise.get_cur_muscle(self.user_id, 'chest')
        cur_muscle.update_points(cur_point + points)
        self.exercise_name = 'push_ups'
        self.points = points
        self.save_exercise_to_database()

    def chest_flies(self, points):
        cur_muscle, cur_point = Exercise.get_cur_muscle(self.user_id, 'chest')
        cur_muscle.update_points(cur_point + points)
        self.exercise_name = 'chest_flies'
        self.points = points
        self.save_exercise_to_database()

    def dumbbell_press(self, points):
        cur_muscle, cur_point = Exercise.get_cur_muscle(self.user_id, 'chest')
        cur_muscle.update_points(cur_point + points)
        self.exercise_name = 'dumbbell_press'
        self.points = points
        self.save_exercise_to_database()

    # class back(Muscle): #גב

    def pull_ups(self, points):
        cur_muscle, cur_point = Exercise.get_cur_muscle(self.user_id, 'back')
        cur_muscle.update_points(cur_point + points)
        self.exercise_name = 'pull_ups'
        self.points = points
        self.save_exercise_to_database()

    def rows(self, points):
        cur_muscle, cur_point = Exercise.get_cur_muscle(self.user_id, 'back')
        cur_muscle.update_points(cur_point + points)
        self.exercise_name = 'rows'
        self.points = points
        self.save_exercise_to_database()

    def lat_pulldowns(self, points):
        cur_muscle, cur_point = Exercise.get_cur_muscle(self.user_id, 'back')
        cur_muscle.update_points(cur_point + points)
        self.exercise_name = 'lat_pulldowns'
        self.points = points
        self.save_exercise_to_database()

    # class Shoulders(Muscle):  # כתפיים
    def shoulder_press(self, points):
        cur_muscle, cur_point = Exercise.get_cur_muscle(self.user_id, 'shoulders')
        cur_muscle.update_points(cur_point + points)
        self.exercise_name = 'shoulder_press'
        self.points = points
        self.save_exercise_to_database()

    def lateral_raises(self, points):
        cur_muscle, cur_point = Exercise.get_cur_muscle(self.user_id, 'shoulders')
        cur_muscle.update_points(cur_point + points)
        self.exercise_name = 'lateral_raises'
        self.points = points
        self.save_exercise_to_database()

    def front_raises(self, points):
        cur_muscle, cur_point = Exercise.get_cur_muscle(self.user_id, 'shoulders')
        cur_muscle.update_points(cur_point + points)
        self.exercise_name = 'front_raises'
        self.points = points
        self.save_exercise_to_database()

    # class Biceps(Muscle): # יד קדמית
    def bicep_curls(self, points):
        cur_muscle, cur_point = Exercise.get_cur_muscle(self.user_id, 'biceps')
        cur_muscle.update_points(cur_point + points)
        self.exercise_name = 'bicep_curls'
        self.points = points
        self.save_exercise_to_database()

    def hammer_curls(self, points):
        cur_muscle, cur_point = Exercise.get_cur_muscle(self.user_id, 'biceps')
        cur_muscle.update_points(cur_point + points)
        self.exercise_name = 'hammer_curls'
        self.points = points
        self.save_exercise_to_database()

    # class Triceps(Muscle):  #  יד אחורית
    def triceps_dips(self, points):
        cur_muscle, cur_point = Exercise.get_cur_muscle(self.user_id, 'triceps')
        cur_muscle.update_points(cur_point + points)
        self.exercise_name = 'triceps_dips'
        self.points = points
        self.save_exercise_to_database()

    def triceps_pushdowns(self, points):
        cur_muscle, cur_point = Exercise.get_cur_muscle(self.user_id, 'triceps')
        cur_muscle.update_points(cur_point + points)
        self.exercise_name = 'triceps_pushdowns'
        self.points = points
        self.save_exercise_to_database()

    # class Quadriceps(Muscle):  #  4 ראשי
    def squats(self, points):
        cur_muscle, cur_point = Exercise.get_cur_muscle(self.user_id, 'quadriceps')
        cur_muscle.update_points(cur_point + points)
        self.exercise_name = 'squats'
        self.points = points
        self.save_exercise_to_database()

    def lunges(self, points):
        cur_muscle, cur_point = Exercise.get_cur_muscle(self.user_id, 'quadriceps')
        cur_muscle.update_points(cur_point + points)
        self.exercise_name = 'lunges'
        self.points = points
        self.save_exercise_to_database()

    def leg_press(self, points):
        cur_muscle, cur_point = Exercise.get_cur_muscle(self.user_id, 'quadriceps')
        cur_muscle.update_points(cur_point + points)
        self.exercise_name = 'leg_press'
        self.points = points
        self.save_exercise_to_database()

    # class Hamstrings(Muscle):  # ירכיים
    def deadlifts(self, points):
        cur_muscle, cur_point = Exercise.get_cur_muscle(self.user_id, 'hamstrings')
        cur_muscle.update_points(cur_point + points)
        self.exercise_name = 'deadlifts'
        self.points = points
        self.save_exercise_to_database()

    def hamstring_curls(self, points):
        cur_muscle, cur_point = Exercise.get_cur_muscle(self.user_id, 'hamstrings')
        cur_muscle.update_points(cur_point + points)
        self.exercise_name = 'hamstring_curls'
        self.points = points
        self.save_exercise_to_database()

    # class Calves(Muscle): # תאומים
    def calf_raises(self, points):
        cur_muscle, cur_point = Exercise.get_cur_muscle(self.user_id, 'calves')
        cur_muscle.update_points(cur_point + points)
        self.exercise_name = 'calf_raises'
        self.points = points
        self.save_exercise_to_database()

    # class Abdominal(Muscle):# בטן
    def planks(self, points):
        cur_muscle, cur_point = Exercise.get_cur_muscle(self.user_id, 'abdominal')
        cur_muscle.update_points(cur_point + points)
        cur_muscle, cur_point = Exercise.get_cur_muscle(self.user_id, 'back')
        cur_muscle.update_points(cur_point + points)
        self.exercise_name = 'planks'
        self.points = points
        self.save_exercise_to_database()

    def sit_ups(self, points):
        cur_muscle, cur_point = Exercise.get_cur_muscle(self.user_id, 'abdominal')
        cur_muscle.update_points(cur_point + points)
        self.exercise_name = 'sit_ups'
        self.points = points
        self.save_exercise_to_database()

    def russian_twists(self, points):
        cur_muscle, cur_point = Exercise.get_cur_muscle(self.user_id, 'abdominal')
        cur_muscle.update_points(cur_point + points)
        self.exercise_name = 'russian_twists'
        self.points = points
        self.save_exercise_to_database()

    def save_exercise_to_database(self):
        conn = sqlite3.connect('data.db')
        c = conn.cursor()
        c.execute("INSERT INTO exercise_data (user_id, exercise_name, points, exercise_date) VALUES (?, ?, ?, ?)",
                  (self.user_id, self.exercise_name, self.points, self.exercise_date))
        conn.commit()






