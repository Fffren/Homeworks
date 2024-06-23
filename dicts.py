x_men={"Rogue": 1,"wolverine":2}
x_men["wolverine"] = 2
print(x_men)
print(x_men["Rogue"])
x_men[3] ="ciclop"
x_men[4] = "beast"
print (x_men)
print (x_men[3])
print (x_men[4])
del x_men["Rogue"]
print (x_men)
x_men.update({"Pops":10,
              "Pepa":20,
              "Mops":30})
print(x_men.get("lul", "Такого значения нет"))
x_men.pop("Pops")
print(x_men)
print(x_men.keys())
print(x_men.values())
print(x_men.items())
#Тут начинается часть про множества
set_1={1,2,3,4,5,6,7,1,1,12,2,2,3,4, 'pops', 'mops',True, (123,124)}
list_1= [1,1,2,3,2,4,5,5,6,7]
set_2=set(list_1)
print(set_1)
print(list_1)
print(set_2)
set_2.discard(1)
print(set_2)
set_2.add(224)
print(set_2)

