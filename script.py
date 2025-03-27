from linkedlist import LinkedList
from node import *
from restaurantData import *


def insert_food_type():
    food_type_list = LinkedList()
    for food_type in types:
        food_type_list.append(food_type)
    return food_type_list

def insert_restauraunt_data():
    restauraunt_data_list = LinkedList()
    for food_type in types:
        restauraunt_sublist = LinkedList()
        for restauraunt in restaurant_data:
            if restauraunt[0] == food_type:
                restauraunt_sublist.append(restauraunt)
        restauraunt_data_list.append(restauraunt_sublist)
    return restauraunt_data_list


food_list = insert_food_type()
restauraunt_list = insert_restauraunt_data()


