import muscle, exercises
import pandas as pd

# muscle_list = ['user_name', 'cardiopulmonary_endurance', 'chest', 'back',
#                    'shoulders', 'biceps', 'triceps', 'quadriceps',
#                    'hamstrings', 'calves', 'abdominal']
#
# new_list = ['user_name']
# for elem in muscle_list[1:]:
#     new_list.append(elem + '__point')
#     new_list.append(elem + '__date')
#     new_list.append(elem + '__rest')
#
# df = pd.DataFrame(columns=new_list)
# df.to_csv('data.csv')

class user_data():
    muscle_list = ['cardiopulmonary_endurance', 'chest', 'back',
                   'shoulders', 'biceps', 'triceps', 'quadriceps',
                   'hamstrings', 'calves', 'abdominal']

    def __init__(self, username, weight=70, height=1.75):
        self.user_name = username
        self.values = self.get_data(username)
        self.height = height
        self.weight = weight

    def get_data(self, username, patch='data.csv'):
        data = pd.read_csv(patch)
        user_set = data['user_name']
        if username in user_set:
            user_val = data.loc[data.user_name == username].tolist()[1:]
            return {user_data.muscle_list[i]: muscle.Muscle(tuple(user_val[i*3:(i+1)*3])) \
                    for i in range(len(user_data.muscle_list))}
        else:
            return {k: muscle.Muscle() for k in user_data.muscle_list}

    def save_data(self, patch='data.csv'):
        df = pd.read_csv(patch)
        val_list = [self.user_name]
        for key in user_data.muscle_list:
            val_list.append(self.values[key].getvalue())
        if self.user_name in df['user_name'].tolist():
            df.loc[df['user_name'] == self.user_name] = val_list
        else:
            df.iloc[len(df.index)] = val_list
        df.to_csv('data.csv')

    def print_val(self):
        for key in user_data.muscle_list:
            print(key, self.values[key].getvalue())


ari = user_data('ari')
ari.save_data()
