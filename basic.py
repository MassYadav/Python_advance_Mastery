

# a = [1, 2, 3,11]
# for i in range(len(a) - 1):
#     if a[i] < a[i + 1]:
#         continue
#     else:
#         print("not sorted list ")
#         break  
# else:
#     print("sorted list")   


# for i in range(len(t)):
#     print(t[i])  


# # set , unordered collection of unique elements
# s = {1, 2, 3, 4, 4}
# print(s)  # Output: {1, 2, 3, 4}

# #set methods 

# #dictionary 
# d = {'name': 'Alice', 'age': 30, 'city': 'New York'}
# print(d['name'])  # Output: Alice

# a = int(input(f"Enter a number: "))

# try:
#        print(10/a)

# except Exception as err:
#        print(f"sorry error accured:--  {err}")
# else:
#      print("no error accured") 

# finally:
#      print("this will always execute")      

# print("ok i diveded it successfully")





# age = int(input("Enter your age: "))

# try:
#     if age < 10 or age > 18:
#        raise ValueError("you are not eligible for this program")
#     else:
#        print("you are eligible for this program")
# except Exception as err:
#    print(f"Error: {err}")


# print("ok i am done")

# file handlings 

# p = open(r"basic.py", "r")
# print(p.read())

r = open("batman.txt","a")
r.write("i am batman demon")
r.close()
