import muscle
import pandas as pd

# muscle_list = ['user_name', 'cardiopulmonary_endurance', 'chest', 'back',
#                    'shoulders', 'biceps', 'triceps', 'quadriceps',
#                    'hamstrings', 'calves', 'abdominal']
#
# new_list = ['user_name']
# for elem in muscle_list[1:]:
#     new_list.append(elem + '_point')
#     new_list.append(elem + '_date')
#     new_list.append(elem + '_rest')
#
# df = pd.DataFrame(columns=new_list)
# df.to_csv('data.csv')

class user_data():
    muscle_list = ['cardiopulmonary_endurance', 'chest', 'back',
                   'shoulders', 'biceps', 'triceps', 'quadriceps',
                   'hamstrings', 'calves', 'abdominal']

    def __init__(self, username):
        self.user_name = username
        self.values = self.get_data(username)

    def get_data(self, username, patch='data.csv'):
        data = pd.read_csv(patch)
        user_set = data['user_name']
        if username in user_set:
            return dict(data[username])
        else:
            return {k: muscle.Muscle() for k in user_data.muscle_list}

    def save_data(self, patch='data.csv'):
        df = pd.read_csv(patch)
        df.loc[df['user_name'] == self.user_name] = self.values
        df.to_csv('data.csv')


    def __str__(self):

        return ''.join(self.user_name) + "\n" + ' ;'.join(self.values)


ari = user_data('ari')
print(ari)