import users
import exercises

def calculate_bmi(weight, height):
    # Calculating BMI
    bmi = weight / (height ** 2)
    return bmi

def set_program_type(bmi):
# Determining the recommendation based on BMI value
    if bmi < 20:
        recommendation = "The recommendation for you is to do strength training mainly and gain weight. 1"
    elif 20 <= bmi < 30:
        recommendation = "The recommendation for you is to combine strength training and aerobic activity. 2"
    else:
        recommendation = "The recommendation for you is to do mainly aerobic activity. 3"

    type = input(recommendation)
    return type

def create_program(type):
    if type == '1':
        a = [Quadriceps.squats(), Quadriceps.lunges(), Quadriceps.leg_press(), Hamstrings.deadlifts(), Hamstrings.hamstring_curls(),Calves.Calf_raises(), back.pull_ups(), back.rows(), back.lat_pulldowns(), Biceps.bicep_curls(), Biceps.hammer_curls()]
        b = [chest.bench_press(), chest.push_ups(), chest.chest_flyes(), chest.dumbbell_press(), Shoulders.shoulder_press(), Shoulders.lateral_raises(), Shoulders.front_raises(), Triceps.Tricep_dips(), Triceps.tricep_pushdowns(), Abdominals.planks(), Abdominals.sit_ups(), Abdominals.Russian_twists()]

    elif type == '2':
        a = [Quadriceps.squats(), Quadriceps.lunges(), Quadriceps.leg_press(), Hamstrings.deadlifts(), Hamstrings.hamstring_curls(),Calves.Calf_raises(), back.pull_ups(), back.rows(), back.lat_pulldowns(), Biceps.bicep_curls(), Biceps.hammer_curls(), chest.bench_press(), chest.push_ups(), chest.chest_flyes(), chest.dumbbell_press(), Shoulders.shoulder_press(), Shoulders.lateral_raises(), Shoulders.front_raises(), Triceps.Tricep_dips(), Triceps.tricep_pushdowns(), Abdominals.planks(), Abdominals.sit_ups(), Abdominals.Russian_twists()]
        b = [Cardiopulmonary.running(), Cardiopulmonary.cycling(), Cardiopulmonary.swimming()]

    elif type == '3':
        a = [Cardiopulmonary.running(), Cardiopulmonary.cycling(), Cardiopulmonary.swimming()]
        b = a
    return [a, b]




ari.weight()
