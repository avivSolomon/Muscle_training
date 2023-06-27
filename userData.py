import muscle
import sqlite3

def create_db():
    # create users table and muscles table and save it to data.db
    conn = sqlite3.connect('data.db')
    c = conn.cursor()
    c.execute("""CREATE TABLE IF NOT EXISTS users (
                id integer PRIMARY KEY AUTOINCREMENT UNIQUE,
                user_name TEXT,
                height REAL,
                weight REAL
                )""")
    c.execute("""CREATE TABLE IF NOT EXISTS muscles (
                user_id INTEGER,
                muscle_name TEXT,
                points REAL,
                date REAL,
                rest_time REAL,
                FOREIGN KEY (user_id) REFERENCES users(id)
                )""")
    conn.commit()
    conn.close()


class UserData:
    muscle_list = ['cardiopulmonary_endurance', 'chest', 'back',
                   'shoulders', 'biceps', 'triceps', 'quadriceps',
                   'hamstrings', 'calves', 'abdominal']

    def __init__(self, username, weight=70, height=1.75):
        self.user_name = username
        self.height = height
        self.weight = weight
        self.values = [muscle.Muscle(name) for name in UserData.muscle_list]
        # self.id = UserData.id

    def get_name(self):
        return self.user_name

    def get_height(self):
        return self.height

    def get_weight(self):
        return self.weight

    def get_muscle(self, muscle_name):
        for cur_muscle in self.values:
            if cur_muscle.get_name() == muscle_name:
                return cur_muscle
        return None

    def get_muscle_list(self):
        return self.values

    def update_muscle(self, muscle_name, points, date, rest_time):
        for cur_muscle in self.values:
            if cur_muscle.get_name() == muscle_name:
                cur_muscle.update_points(points, date, rest_time)
                return True
        return False

    def update_height(self, height):
        self.height = height

    def update_weight(self, weight):
        self.weight = weight

    def update_name(self, name):
        self.user_name = name

    def save_data(self):
        conn = sqlite3.connect('data.db')
        c = conn.cursor()
        c.execute("INSERT INTO users VALUES (?, ?, ?, ?)", (self.id, self.user_name, self.height, self.weight))
        for cur_muscle in self.values:
            c.execute("INSERT INTO muscles VALUES (?, ?, ?, ?, ?)", (self.id, cur_muscle.get_name(), cur_muscle.get_point(), cur_muscle.get_date(), cur_muscle.get_rest_time()))
        conn.commit()
        conn.close()

    def load_data(self):
        conn = sqlite3.connect('data.db')
        c = conn.cursor()
        c.execute("SELECT * FROM users WHERE user_name=?", (self.user_name,))
        user_data = c.fetchone()
        self.id = user_data[0]
        self.height = user_data[2]
        self.weight = user_data[3]
        c.execute("SELECT * FROM muscles WHERE user_id=?", (self.id,))
        muscle_data = c.fetchall()
        for i in range(len(muscle_data)):
            self.values[i].update_points(muscle_data[i][2], muscle_data[i][3], muscle_data[i][4])
        conn.close()


    # def get_data(self, username, patch='data.csv'):
    #     data = pd.read_csv(patch)
    #     user_set = data['user_name']
    #     if username in user_set:
    #         user_val = data.loc[data.user_name == username].tolist()[1:]
    #         return {UserData.muscle_list[i]: muscle.Muscle(tuple(user_val[i * 3:(i + 1) * 3])) \
    #                 for i in range(len(UserData.muscle_list))}
    #     else:
    #         return {k: muscle.Muscle() for k in UserData.muscle_list}
    #
    #
    def print_val(self):
        for cur_muscle in self.values:
            print(f'muscle name: {cur_muscle.get_name()}\n\t point: {cur_muscle.get_point()}, recent trained at: {cur_muscle.get_date()}, restin time left: {cur_muscle.get_rest_time()}')


ari = UserData('ari')
# ari.update_muscle('chest', 10, 2020, 10)
# ari.load_data()
# ari.save_data()
ari.print_val()


# show data in data.db
def show_data():
    conn = sqlite3.connect('data.db')
    c = conn.cursor()
    c.execute("SELECT * FROM users")
    print(c.fetchall())
    c.execute("SELECT * FROM muscles")
    print(c.fetchall())
    conn.close()
