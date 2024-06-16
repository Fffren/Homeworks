motorcycles= ['honda', 'yamaha', 'suzuki']
motorcycles[0]='ducati'
print (motorcycles)
motorcycles.append('ducati')
print (motorcycles)
friends= []
friends.append('Leha')
friends.append('Kolyan_1')
friends.append('Max')
print(friends)
cars= []
cars.append('lanos')
cars.append('zhigul')
cars.append('toyta')
print(cars)
dishes=['rolli', 'pizza', 'pirogi']
dishes.insert(0, 'burgers')
print(dishes)
del dishes[3]
print(dishes)
dogs =['mops', 'ovcharka', 'pitbull', 'bulterier']
del dogs[3]
techs=['mobilephones','tv','fridges']
popped_tech= techs.pop()
print(techs)
print(popped_tech)
mopeds=['hyundai','honda','chevrolet']
last_owned=mopeds.pop()
print(f"The last moped I owned was a {last_owned.title()}.")
