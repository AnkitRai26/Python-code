#List in python
# A built in data type that stores set of values.
# It can store elements of different types (integer,float,string, etc).

# student = ["Ankit", 27, 6, "Delhi"] #muteable(change) and string is unmuteable 
# print(student[0])
# student[0] = "Ankit Rai"
# print(student)

#List Slicing similar to string slicing
# list = [1,2,3,4,5] print(list[1:4]), output is 2,3,4

#List Methods
#List (list = [2,1,3]) type append(4) adds one element at the end 2,1,3,4, sort()123, reverse()312,
# sort(reverse=True) 3,2,1. insert() insert element at index)
# remove first occurrence of element and pop particular element of these index remove

#list = [1,4,2,3]
# print(list.append(5))
# print(list.sort())
# print(list.sort(reverse=True))
#print(list.reverse())
#print(list.insert(1,6)) #inset(index no. , value)
#print(list.remove(4))
#print(list.pop(3))
#print(list)


# -------- Tuples In Python -------
# A built in data type that lets us create immutable(unchanged) sequences of values.
# In tuple we use parentheses () and In list we use square [] 

#tup = () # its blank tuple
#tup = (1,) # for single tuple we use value then , otherwise he read integer or string
# In tuple everything is same like list

# ------Tuple Methods ----- tup = (2,1,3,1)
#tup.index(el) return index of first occurrences tup.index(1) is 1
# tup.count(el) return total occurrences tup.count(1) is 2

# tup = (2,1,3,1)
# print(tup.count(1)) 

#------Method 1-----
# movies = []
# movie1 = input("Enter your First movvi: ")
# movie2 = input("Enter your Second movie: ")
# movie3 = input("Enter your third movie:")

# movies.append(movie1)
# movies.append(movie2)
# movies.append(movie3)
# print(movies)

#------Method 2-----
# movies = []
# movies.append(input("Enter your 1st movie: "))
# movies.append(input("Enter your 2nd movies: "))
# movies.append(input("Enter your 3nd movies: "))

# print(movies)

# Palindrome when you read starting of the list and end of list are same like ma'am, [1,2,3,2,1]

# list1  = [1,2,3]
# list2 = [1,2,3]

# copy_list1 = list1.copy()
# copy_list1.reverse()

# if(copy_list1 == list1):
#     print("It's palindrome")
# else:
#     print("It's not palindrome")  

#tup = ("C","D","A","A","B","B","A")
tup = ["C","D","A","A","B","B","A"]

print(tup.count("A"))
tup.sort()
print(tup)

