# name = input('Введите ваше имя:')
# if name == 'Urban' or 'urban':
#     print("Hello administrator")
# if name == 'Денис':
#     print ('Здравствуйте, преподаватель')
# else:
#     print("Привет", name)
number = int(input("Введите число:")) #Fizz, Buzz, FizzBuzz
if number % 3 == 0 and number % 5 ==0:
    print('FizzBuzz')
if number % 3 == 0:
    print('Fizz')
elif number % 5 == 0:
    print('Buzz')
else:
    print("Число не корректно")

