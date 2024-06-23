my_dict={"dish_1":"sushi", "dish_2":"pizza", "dish_3":"burger"}
print (my_dict)
my_dict["dish_1"]="sushi"
my_dict["dish_5"]="pasta"
print(my_dict)
my_dict["Denis"]=821738213
my_dict["Volk"]=9281398213
poped_dish= my_dict.pop("dish_3")
my_dict.pop("dish_2")
print(poped_dish)
print(poped_dish.items())