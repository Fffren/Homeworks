food = ["apple", "coconut", "banana"]
print(food[0])
food[0] = "peach"
print(food)
food.append("pineapple")
food.extend(["string",2])
print(food)
food.remove("banana")
print(food)
print("banana" not in food)
print(food[0:-1])
tuple_1 = 1, 2, 3,4
tuple_2= (1, 2, 3, 4)
tuple_3=tuple([1,2,3,4])
print(type(tuple_3))
tuple_5=([1, 2], 3)
tuple_5[0][0]=5
print(tuple_5)
