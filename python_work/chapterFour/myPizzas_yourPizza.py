pizza_list = ['cheese', 'pepperoni', 'veggie']

friendsPizzaList = pizza_list[:]

pizza_list.append('basil')
friendsPizzaList.append('sausage')




print('My favorite pizzas are:')
for pizza in pizza_list:
    print(pizza)

print('\nMy friends favorite pizzas are:')
for pizza in friendsPizzaList:
    print(pizza)