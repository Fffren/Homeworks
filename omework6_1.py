my_dict={"dish_1":"sushi", "dish_2":"pizza", "dish_3":"burger"}
print ("Список еды:", my_dict)
existing_key="dish_1"
non_existing_key="dish_5"
value_existing=my_dict.get(existing_key)
value_non_existing=my_dict.get(non_existing_key)
print(f"Значение для существующего ключа '{existing_key}': {value_existing}")
print(f"Значение для несуществующего ключа '{non_existing_key}': {value_non_existing}")
my_dict["dish_10"]="pasta"
my_dict["dish_11"]="pelmeni"
print(f"Словарь после добавления новых значений:{my_dict}")
removed_key="dish_3"
removed_value = my_dict.pop(removed_key, None)
print("Окончательные изменения в словаре:", my_dict)