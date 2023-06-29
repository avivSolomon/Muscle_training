from exercises import Exercise

class Program_training:

    def __init__(self, gym_manager, user_id):
        self.gym_manager = gym_manager
        self.user_id = user_id

    # Determining the recommendation based on BMI value
    def set_program_type(self, bmi):
        program_type = 'a'
        if bmi < 20:
            recommendation = """The recommendation for you is to do strength \n
                             training mainly and gain weight. 1"""
        elif 20 <= bmi < 30:
            recommendation = """The recommendation for you is to combine strength \n
                             training and aerobic activity. 2"""
        else:
            recommendation = """The recommendation for you is to do mainly aerobic \n
                              activity. 3"""
        while program_type not in ['', '1', '2', '3']:
            program_type = input(recommendation)
        return int(program_type) if program_type != '' else int(recommendation[-1])

    def create_program(self, program_type):
        user = Exercise(self.gym_manager, self.user_id)
        a, b = [], []
        if program_type == 1:
            a = [user.squats, user.lunges, user.leg_press, user.deadlifts,
                 user.hamstring_curls, user.calf_raises, user.pull_ups,
                 user.rows, user.lat_pulldowns, user.bicep_curls,
                 user.hammer_curls]

            b = [user.bench_press, user.push_ups, user.chest_flies,
                 user.dumbbell_press, user.shoulder_press, user.lateral_raises,
                 user.front_raises, user.triceps_dips, user.triceps_pushdowns,
                 user.planks, user.sit_ups, user.russian_twists]

        elif program_type == 2:
            a = [user.squats, user.lunges, user.leg_press, user.deadlifts,
                 user.hamstring_curls, user.calf_raises, user.pull_ups,
                 user.rows, user.lat_pulldowns, user.bicep_curls,
                 user.hammer_curls, user.bench_press, user.push_ups, user.chest_flies,
                 user.dumbbell_press, user.shoulder_press, user.lateral_raises,
                 user.front_raises, user.triceps_dips, user.triceps_pushdowns,
                 user.planks, user.sit_ups, user.russian_twists]

            b = [user.running, user.cycling, user.swimming]

        elif program_type == 3:
            a = [user.running, user.cycling, user.swimming]
            b = [exercise for exercise in a]

        return a, b

