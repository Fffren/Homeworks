immutable_var ="король-лич", 12, False, 12.5
print (immutable_var)
#При попытке изменить значение в кортеже immutable_var, система выдает ошибку,
# так как значения в кортеже не изменяемы
mutable_list=["Люди икс", "Человек-паук","Марвел"]
mutable_list[0]= 1
mutable_list[1]=2
mutable_list[2]=True
print (mutable_list)