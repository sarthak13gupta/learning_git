#Create tuple
fruits = ('Apples' , 'Oranges' , 'Grapes')

#single value needs a trailing comma
fruits2 = ('Apples',)

#Get value
print(fruits[1])

#Can't change value 
#fruits[0] = 'Pears'

#delete tuple
del fruits2

#Get length
print(len(fruits))


# A Set is a collection which is unordered and unindexed . No duplicate members.

#Create set
fruits_set = {'Apples' , 'Oranges' , 'Mango'}

#check if in set 
print('Apples' in fruits_set)

#Add to set
fruits_set.add('Grape')

#Remove from set
fruits_set.remove('Grape')

#Add duplicat
fruits_set.add('Apples')

#Clear set
#fruits_set.clear()

# delete
# del fruits_set

print(fruits_set)

