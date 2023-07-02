from app.controller.training_program_controller import TrainingProgramController
import sqlite3

class TrainingProgramView:
    def __init__(self):
        self.training_program_controller = TrainingProgramController()

    def create_program(self):
        name = input("Enter program name: ")
        duration = int(input("Enter program duration (in days): "))

        # Create a new TrainingProgram instance
        program = self.training_program_controller.create_program(name, duration)

        return program

    def add_exercise_to_program(self, program):
        exercise_name = input("Enter exercise name: ")
        exercise_duration = int(input("Enter exercise duration (in minutes): "))
        exercise_intensity = input("Enter exercise intensity: ")

        # Create a new Exercise instance
        exercise = self.training_program_controller.create_exercise(exercise_name, exercise_duration, exercise_intensity)

        # Add the exercise to the training program
        self.training_program_controller.add_exercise_to_program(program, exercise)
        print("Exercise added to the program.")

    def display_program_details(self, program):
        program_details = program.get_program_details()
        print(program_details)

    def manage_training_program(self):
        program = self.create_program()

        while True:
            print("\n1. Add Exercise")
            print("2. Display Program Details")
            print("3. Back")

            choice = input("Enter your choice: ")
            if choice == "1":
                self.add_exercise_to_program(program)
            elif choice == "2":
                self.display_program_details(program)
            elif choice == "3":
                break
            else:
                print("Invalid choice. Please try again.")


# Additional code for user interface related to training program management

if __name__ == "__main__":
    conn = sqlite3.connect(r"C:\Users\ariya\PycharmProjects\Muscle_training\app\database\muscle_training.db")
    # c = conn.cursor()
    # c.execute("schema")


    # Create a cursor object to interact with the database
    cursor = conn.cursor()

    # Query the sqlite_master table to get the schema information
    cursor.execute("SELECT name, sql FROM sqlite_master WHERE type='table'")

    # Fetch all the table information
    tables = cursor.fetchall()

    # Print the schema for each table
    for table in tables:
        table_name = table[0]
        table_schema = table[1]
        print("Table Name:", table_name)
        print("Table Schema:", table_schema)
        print("\n")

    # Close the cursor and the database connection
    cursor.close()
    conn.close()

    # c.execute("SELECT * FROM exercise")
    # print(c.fetchall())



