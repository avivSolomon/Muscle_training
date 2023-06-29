from user import User
from user_controller import UserController
from user_view import UserView
from database import Database

# Create an instance of the Database class
db = Database("users.db")

# Create tables if they don't exist
create_users_table_query = """
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    email TEXT NOT NULL,
    password TEXT NOT NULL
)
"""
db.execute_query(create_users_table_query)

# Instantiate the UserView, UserController, and User classes
user_view = UserView()
user_controller = UserController()

while True:
    print("\n1. Register User")
    print("2. Login User")
    print("3. Manage Profile")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        user_controller.register_user()
    elif choice == "2":
        user_controller.login_user()
    elif choice == "3":
        user_controller.manage_profile()
    elif choice == "4":
        break
    else:
        print("Invalid choice. Please try again.")

# Close the database connection
db.disconnect()
