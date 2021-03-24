# Create list
numbers = [1,2,3,4,5]
fruits = ['Apples' , 'Oranges' , 'Grapes' , 'Pears']

#use a constructor
#numbers2 = list((1,2,3,4,5))

# Get a value
print(fruits[1])

#Get length
print(len(fruits))

#Append to the list
fruits.append('Mangoes')

#Remove from list
fruits.remove('Grapes')

#Insert into position
fruits.insert(2,'Strawberries')

#Remove with pop
fruits.pop(2)

#Reverse list
fruits.reverse()

#Sort list
fruits.sort()

#Reverse sort
fruits.sort(reverse=True)

#change value
fruits[0] = 'Blueberries'

print(fruits)