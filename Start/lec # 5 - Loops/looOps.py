# count = 5
# while count>=1:
#     print("loops are started from here", count)
#     count-=1

# print(count)   

# Q-3
# Print a table of number N

# n = int(input("enter a number for table"))

# i = 1

# while i<=10:
#     result = n*i
#     print(f'{n} x {i} = {result}') 
#     i+=1

# Q-4 
# Print the elements of following list using loop

# number_list = [1,4,9,16,25,36,49,64,81,100]
# print(number_list)
# range = len(number_list)

# idx = 0
# while idx<=range-1:
#     print(number_list[idx], idx)
#     idx+=1

# Q -5 find a number X from in this tuple using loop

# x = int(input('Enter a desired number for searching : '))
# num_tuple = (1,4,9,16,25,36,49,64,81,100)

# i = 0

# while i<len(num_tuple):
#     if(num_tuple[i] == x):
#         print(f'Your entered the number {x} at Index {i}')
#         break 
#     else:
#         print('Does NOT exist')
#     i+=1

  
# CONTINUE - SKIP in loop & also find even or odd number

# i = 0

# while(i<=10):
#     if(i%2==0):
#         i+=1
#         continue # Skip this element/item
#     print(i)
#     i+=1

# For loop

# str = "Muhammad Jamshaid Aziz"

# for letter in str:
#     print(letter)
# else:
#     print("END")

# Q - 7 - Search for an input number X in tuple

# x = int(input('Enter a number for searching ...'))

# tup = (1,4,9,16,25,36,49,64,81,100,9)

# for value in tup:
#     if(value == x):
#         print(value)
#         break
#     else:
        
#         print('not found yet')
# else:
#     print('Does not EXIST')

# Range() Function 

# for i in range(101, 0, -5):
#     print(i)

# Print a table of N input number

# n = int(input('Enter a number here for print the Table - > '))

# for i in range(1, 11):
#     result = n*i
#     print(f'{n} x {i} = {result}')
#     print('Used Pass statement')

# Q-8 => find the sume of natural numbers 

# n = 7
# sum = 0
# for i in range(1, n+1, 3):
#     sum+=i
    
# print(f'Total sum of natural numbers is : {sum}')

# Q-8 => find the factorial of natural number x

x = 5
fact = 1
for i in range(1, x+1):
    fact *= i
print(f'Factorial of number X is : {fact}')

fact = 1
x = 5
i = 1
while(i <= x):
    fact *=i
    i+=1
print(f'factorial of X is : {fact}')






