# -----------Function and Recursion------------

# -------------Function------
# Block of statement that perform a specific task.

# def sum_One(a,b):
#     sum = a + b
#     print(sum)
#     return(sum)

# sum_One(10,5) #recall the function
# sum_One(11,2)

# function definition
# def cal_sum(a,b): # parameters
#     return a + b

# sum = cal_sum(10,15) #function call (argument)
# print(sum)

# average of 3 number
# def avg_sum(a,b,c):
#     return (a + b + c)/3
# avg = avg_sum(7,14,21)
# avg1 = avg_sum(1,2,3)
# print(avg)
# print(avg1)

# -----------Type of function in python ------------
# there are two type 1)Built, 2)User defined function

# Built Function 1)print(), 2)len(), 3)type(), 4)range()
# Print(), In sep and end

# User Defined Function (written by user)

# ------Default Parameters-------
# Assigning a default value to parameter, which is used when no argument is passed.
# def cal(a=1,b=1):print(a*b)return(a*b) cal() this called default parameters
# def cal(a,b=1) it can't be cal(a=1,b) this through error


# ques 1
# nums = [1, 2, 3, 4, 5, 6, 7, 8]
# def list_len(list):
#     print(len(list))
    
# list_len(nums)

# ques2
# cities = ["delhi", "Mumbai", "Lucknow", "Gurugram", "Noida"]

# def list_cities(list):
#     for item in list:
#         print(item, end=" ")


# list_cities(cities)

# ques 3 factorial


# def fact_cal(n):
#     fact = 1
#     for el in range(1, n+1):
#         fact *= el
#     print(fact)
# fact_cal(5)        


# ques 4 convert usd to inr

# def usd_ind(usd_val):
#     inr = 95 * usd_val
#     print(usd_val, "USD =", inr, "INR")
# usd_ind(4)

# Odd and even question
# inpt_val = int(input("Enter number here:- "))

# def odd_even(n):
#     if(n % 2 == 0):
#         return ("Even")
#     else:
#         return ("odd")
    
# print(odd_even(inpt_val))

# ------------- Recursion ----------------
# When a function calls itself repeatrdly.

# show is recursive function
# def show(n):
#     if(n == 0): #base case
#         return
#     print(n, end=" ")
#     show(n-1)
# show(5)

# def fact(n):
#     if(n == 0 or n == 1):
#         return 1
#     else:
#         return n * fact(n-1)
    
# print(fact(5))

# Write a recursive function to calculate the sum of first n natural number
# def sum(n):
#     if(n == 0):
#         return 0
#     return sum(n-1) + n
# print(sum(10))

# Write a recursive function to print all elements in a list.
def print_list(list, idx=0):
    if(idx == len(list)):
        return
    
    print(list[idx], end=" ")
    print_list(list, idx+1)
name = ["Ankit", "Ankur", "Rai", "Rai2"]
print_list(name)
