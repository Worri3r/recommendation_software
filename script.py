from linkedlist import LinkedList
from restaurantData import *


def insert_food_type():
    food_type_list = LinkedList()
    for food_type in types:
        food_type_list.insert(food_type)
    return food_type_list

def insert_restauraunt_data():
    restauraunt_data_list = LinkedList()
    for food_type in types:
        restauraunt_sublist = LinkedList()
        for restauraunt in restaurant_data:
            if restauraunt[0] == food_type:
                restauraunt_sublist.insert(restauraunt)
        restauraunt_data_list.insert(restauraunt_sublist)
    return restauraunt_data_list


food_list = insert_food_type()
restauraunt_list = insert_restauraunt_data()


select_food_type = ""

while len(select_food_type) == 0:

    user_input = str(input("\nWhat type of food would you like?\n Type the beginning of the food.\n")).lower()

    matching_types = []
    head_type_list = food_list.get_head_node()
    while head_type_list is not None:
        if str(head_type_list.get_value()).startswith(user_input):
            matching_types.append(head_type_list.get_value())
        head_type_list = head_type_list.get_next_node()

    for food in matching_types:
        print(food)

    if len(matching_types) == 1:
        choose_type = str(input(f"\nThe found matching type is {matching_types[0]}.\n Do you want to see the restauraunts in the Databank? y for yes and n for no  ")).lower()

        if choose_type == "y":
            select_food_type = matching_types[0]
            print(f"Chosen food type: {select_food_type}")
            head_rest_list = restauraunt_list.get_head_node()
            while head_rest_list.get_next_node() is not None:
                sublist_head = head_rest_list.get_value().get_head_node()
                if sublist_head.get_value()[0] == select_food_type:
                    while sublist_head.get_next_node() is not None:
                        print("--------------------------")
                        print("Name: " + sublist_head.get_value()[1])
                        print("Price: " + sublist_head.get_value()[2] + "/5")
                        print("Rating: " + sublist_head.get_value()[3] + "/5")
                        print("Address: " + sublist_head.get_value()[4])
                        print("--------------------------\n")
                        sublist_head = sublist_head.get_next_node()
                head_rest_list = head_rest_list.get_next_node()

        repeat = str(input("\n Do you want to search for something different?\nType y for yes and n for no.  ")).lower()
        if repeat == "y":
            select_food_type = ""