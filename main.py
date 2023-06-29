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
    # data_base.create_database()
    # create a gym manager
    gym_manager = GymManager()
    # load existing users from data.db to gym_manager V
    gym_manager.load_data()
    # create a new users V
    # gym_manager.create_user("user1", 180, 70)
    # gym_manager.create_user("user2", 170, 60)
    # gym_manager.create_user("user3", 160, 50)

    # get user list V
    user_list = gym_manager.get_user_list()

    # update user V
    # user_list[0].update_muscle("chest", 10)
    # user_list[0].update_muscle("back", 20)

    # print(gym_manager.get_user(0).get_muscle("chest"))

    # testing users methods
    # print(user_list[0].get_name())
    # print(user_list[0].get_height())
    # print(user_list[0].get_weight())
    # print(user_list[0].get_muscle("chest"))
    # print(user_list[0].get_bmi())
    # print(user_list[0].get_muscle_list())
    # user_list[0].update_name("ari")
    # user_list[0].update_height(120)
    # print(user_list[0].get_name())
    # user_list[0].update_weight(50)
    # user_list[0].print_val()
    # for user in user_list:
    #     print(user)
    # # show all data
    # ari_train = Exercise(gym_manager, 0).running(10)
    # ari = gym_manager.get_user(0)
    # ari.print_val()
    data_base.show_all_data()

    # create a new exercise




if __name__ == '__main__':
    main()
