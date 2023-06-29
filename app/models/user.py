class User:
    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.password = password

        # self.height = height
        # self.weight = weight
        # self.bmi = self.weight / ((self.height / 100) ** 2)
        # self.muscles = [Muscle(name) for name in User.muscle_list]
        # self.program = program

    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name

    def get_email(self):
        return self.email

    def set_email(self, email):
        self.email = email

    def get_password(self):
        return self.password

    def set_password(self, password):
        self.password = password


