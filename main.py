from users import User
import data_base
import muscle
from gym_manager import GymManager
from exercises import Exercise
from datetime import date

def main():
    # delete all data
    # data_base.delete_all_data()
    # create new database
    data_base.create_database()
    # create a gym manager
    gym_manager = GymManager()
    # load existing users from data.db to gym_manager
    gym_manager.load_data()
    # create a new users
    gym_manager.create_user("user1", 180, 70)
    gym_manager.create_user("user2", 170, 60)
    gym_manager.create_user("user3", 160, 50)

    # get user list
    user_list = gym_manager.get_user_list()

    # update user
    user_list[0].update_muscle("chest", 10)
    # user_list[0].update_muscle("back", 20)









    for user in user_list:
        print(user)
    # # show all data
    data_base.show_all_data()


if __name__ == '__main__':
    main()
