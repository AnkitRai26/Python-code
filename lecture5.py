# Loops in python
# Loops are used to repeat instruction
# There are two types 1.For and 2.While

# ----------------While lopps -------------------


# i = 1
# while i <= 5:
#     print("Python", i)
#     i+=1

# i = 5
# while i <=1:
#     print(i)
#     i-=1

# i=100
# while i>=1:
#     print(i)
#     i-=1

# i = 1
# while i <= 10:
#     print(i*i)
#     i+=1

# num = 5
# i = 1
# while i <= 10:
#     print(num * i)
#     i+=1

# i = 1
# while i <= 10:
#     print(i*i)
#     i+=1

# question4
# nums = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
# idx = 0
# while idx < len(nums):
#     print(nums[idx])
#     idx += 1

# nums = (1, 4, 9, 16, 25, 36, 49, 64, 81, 100)
# x = 4
# idx = 0
# while idx < len(nums):
#     if(nums[idx] == x):
#         print("Found at idx", idx)
#     idx += 1

# ----- Break and continus

# Stops printing numbers once it reaches 5
# for number in range(1, 10):
#     if number == 5:
#         break  # Exit the loop entirely
#     print(number)

# print("Loop finished!")

# Skips printing the number 5 but prints everything else
# for number in range(1, 7):
#     if number == 5:
#         continue  # Skip the rest of this iteration
#     print(number)

# print("Loop finished!")


# ------Loop in Python ---------------

# Loop are used for sequential traversal. For traversing list, string, tuples etc.

# list = [1, 3, 4, 5, 7]
# tup = (1, 3, 4, 5, 7)
# str = "Ankit Rai"
# for char in str:
#     if(char == "r"):
#         break
#     print("Found",char)

# else:
#     print("N/A")
    

# Ques 1
# x = 9
# idx = 0
# list = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100,9]
# for el in list:
#     if(el == x):
#         print("Number found at:-", idx)
#         break
#     idx += 1
        

# ------- Rnagr() ------------

# Range function returns a srquence of numbers, starting from 0 by default and increments
# by 1(by default) and stops before a specified number.

# range(start?, stop, step?) in 1 to 5 start index 0, end 4,step 1 increase


# for el in range(10): # range(stop)
#     print(el)

# for el in range(2, 10): # range(start, stop)
#     print(el)

# for el in range(2, 10, 2): #range(start, stop, step(incresae how many step))
#     print(el)

# ques 1 for and range
# for el in range(1, 101):
#     print(el)

# # ques 2
# for el in range(100, 0, -1):
    
#     print(el)

#question 3
# n = 3
# for el in range(1,11):
#     print(el*n)


# ------ Pass Statement -------------
# pass is null statement that does nothing. It is used as a placehollder for future code.

# for i in range(5):
#     pass
# print("Some useful work")


# ques1

# n = int(input("Eneter your number here:- "))
# sum =0
# i = 1
# while i<=n:
#     sum += i
#     i+=1
# print("Total sum", sum)
# for i in range(1, n+1):
#     sum += i
# print("total Sum", sum)

# ques2

# n = 5
# val = 1
# for i in range(1, n+1):
#     val *= i
# print("Factorial",val)





