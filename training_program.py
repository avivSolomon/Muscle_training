from users import User
from exercises import Exercise


# Determining the recommendation based on BMI value
def set_program_type(bmi):
    if bmi < 20:
        recommendation = "The recommendation for you is to do strength training mainly and gain weight. 1"
    elif 20 <= bmi < 30:
        recommendation = "The recommendation for you is to combine strength training and aerobic activity. 2"
    else:
        recommendation = "The recommendation for you is to do mainly aerobic activity. 3"

    program_type = input(recommendation)
    return program_type


def create_program(program_type):
    a, b = [], []
    if program_type == '1':
        a = [Exercise.squats, Exercise.lunges, Exercise.leg_press, Exercise.deadlifts,
             Exercise.hamstring_curls, Exercise.calf_raises, Exercise.pull_ups,
             Exercise.rows, Exercise.lat_pulldowns, Exercise.bicep_curls,
             Exercise.hammer_curls]

        b = [Exercise.bench_press, Exercise.push_ups, Exercise.chest_flyes,
             Exercise.dumbbell_press, Exercise.shoulder_press, Exercise.lateral_raises,
             Exercise.front_raises, Exercise.triceps_dips, Exercise.triceps_pushdowns,
             Exercise.planks, Exercise.sit_ups, Exercise.russian_twists]

    elif program_type == '2':
        a = [Exercise.squats, Exercise.lunges, Exercise.leg_press, Exercise.deadlifts,
             Exercise.hamstring_curls, Exercise.calf_raises, Exercise.pull_ups,
             Exercise.rows, Exercise.lat_pulldowns, Exercise.bicep_curls,
             Exercise.hammer_curls, Exercise.bench_press, Exercise.push_ups, Exercise.chest_flyes,
             Exercise.dumbbell_press, Exercise.shoulder_press, Exercise.lateral_raises,
             Exercise.front_raises, Exercise.triceps_dips, Exercise.triceps_pushdowns,
             Exercise.planks, Exercise.sit_ups, Exercise.russian_twists]

        b = [Exercise.running, Exercise.cycling, Exercise.swimming]

    elif program_type == '3':
        a = [Exercise.running, Exercise.cycling, Exercise.swimming]
        b = [exercise for exercise in a]
    return a, b



