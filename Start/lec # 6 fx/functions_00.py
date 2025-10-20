# write a recursive function to print the all elements in the list

# cities = ['Karachi'] # here index = 0 && len is 1
cities = ['Karachi','Lahore','Islamabad','Rawalpindu','Peshawar','Mansehra']  

def show_name(city, index=0):
    if len(city) == 0:
        return 'No city exist in this list'
    elif(index == len(cities)):
        return ' End of cities name'
    print(city[index])

    return show_name(city, index + 1) # here function is calling itself and also return the results.

result = show_name(cities)
print(result)

# Write a recursion function calculate the sum of natural numbers till 

# def sum_natural(n):
#     if(n==0):
#         return 0
#     return sum_natural(n-1) + n

# result = sum_natural(5) 
# print(result)



# Print Fctorial

# def fact(n):
#     if(n==0 or n==1):
#         return 1
#     else:
#         return fact(n-1) * n

# result = fact(4)
# print(result)


# Recurion via function


# def recursion(n):
#     if n==0:
#         return # if we don't write any statement with RETURN then it means we return control/ go out from the function.
#     print(n)
#     recursion(n-1)

# recursion(5)

# write a function if you enter a odd number then function must return Number is event else ODD

# def read_input(prompt):
#     while True:
#         try:
#             return(int(input(prompt)))
#         except ValueError:
#             print('Please enter an integer value')
    

# x = read_input('Enter an integer  :  ')

# def even_odd(n):
#     if n%2 == 0:
#         return 'number is EVEN'
#     else:
#         return 'number is ODD'

# result = even_odd(7)
# print(result)

# Currency convertor

# def convertor(uds_value):
#     pkr_value = uds_value *300
#     print(pkr_value)

# convertor(200)


# write a function to calculate the factorial which is 1x2x3x4 = 4!

# with for in loop
# n = 5
# fact = 1
# for i in range(1, n+1):
#     fact *= i
# print(fact)


# with function
# def calc_fact(n):
#     fact = 1
#     for i in range(1, n+1):
#         fact = fact * i
#         print(fact)

# calc_fact(6)

# list_cities = ['karachi', 'islamabad', 'lahore', 'multan', 'rawalpindi', 'nowshera']

# print cities using function 'print'
# print(list_cities)

# print city using index of list
# print(list_cities[0])
# print(list_cities[2])

# print cities with using for in loop
# for city in list_cities:
#     print(city, end='  ')

# print cities with using function
# def show_cities(cities):
#     for city in cities:
        # print(city)




# cities = ['a','c','f','r','s']
# # length = len(cities)
# # print(length)

# def counted(n):
#     lenth = len(n)
#     print(lenth)

# counted(cities)

# print('Jamshaid', sep = 'hello')
# print('aziz')

# print('Jamshaid', end = ' & ')
# print('aziz')



# def add(a, b=5):
#     sum = a + b
#     print(sum)

# add(9)

# Function with returns value
# def calc_squre(x):
#     return x*x
# result = calc_squre(5)
# print(result)


# function with Parameters & arguments
# def add(a,b):
#     sum =  a + b
#     print(sum)

# add(2, 5)

# function with no parameters & no arguments
# def say():
#     print('Good morning')

# say()