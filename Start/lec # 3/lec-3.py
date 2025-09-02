# user_1 = input("enter your favotite movie name : ")
# user_2 = input("enter your favotite movie name : ")
# user_3 = input("enter your favotite movie name : ")

# favorite_movie = [user_1, user_2, user_3]
# print(favorite_movie)
# print(favorite_movie.reverse())

# alpha = ['a','b','c','b','a']
# print(alpha)
# list1 = alpha.copy()

list_1 = [1,2,3,2,1,7]

copy_list = list_1.copy()
copy_list.reverse()
print(copy_list)

if(copy_list == list_1 ):
    print("list is Palidrome")
else:
    print("Not a palindrome")
