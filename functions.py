#create function
def sayHello(name = 'sarthak'):
    print(f'Hello {name}')

#Return values
def getSum(num1 , num2):
    total = num1 + num2
    return total


#lambda function

getSum = lambda num1, num2: num1+ num2


print(getSum(10,3))


