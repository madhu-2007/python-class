
#inverted  triangle 
# rows = int(input("Enter the row size for the pattern: "))
# for i in range(rows , 0, -1):  
#     for j in range(rows  - i):  
#         print(" ", end=" ")
#     for k in range(1, 2 * i):  
#         print("*", end=" ")
#     print()

# #diamond
# rows=int(input("enter the row size for this pattern"))
# for i in range (0,rows,1):
#     for j in range(rows-i):
#         print(" ",end=" ")
#     for k in range(1,2*i ):
#         print("*",end=" ")
#     print() 

# for i in range(rows , 0, -1):  
#     for j in range(rows  - i):  
#         print(" ", end=" ")
#     for k in range(1, 2 * i):  
#         print("*", end=" ")
#     print()


#  # hollow square pattern
# rows = int(input("Enter the row size for the pattern: "))
# for i in range(1, rows + 1):  
#     for j in range(1, rows + 1):  
#         if i == 1 or i == rows or j == 1 or j == rows : 
#             print("*", end=" ")
#         else:
#             print(" ", end=" ") 
#     print()

# #hollow right angled triangle
# rows = int(input("Enter the row size for the pattern: "))
# for i in range(1, rows + 1):  
#     for j in range(1, i + 1):  
#         if j == 1 or i == rows or i == j:  
#             print("*", end=" ")
#         else:
#             print(" ", end=" ")  
#     print() 

# #hollow inverted right angled triangle
# rows = int(input("Enter the row size for the pattern: "))
# for i in range(rows, 0 ,-1):  
#     for j in range(1, i + 1):  
#         if j == 1 or i == rows or i == j:  
#             print("*", end=" ")
#         else:
#             print(" ", end=" ")  
#     print() 


# # #hollow pyramid pattern
# rows = int(input("Enter the row size for the pattern: "))
# for i in range(1, rows + 1): 
#     for j in range(rows  - i): 
#         print(" ", end=" ")
#     for k in range(1, 2 * i): 
#         if k == 1 or k == 2 * i - 1 or i == rows: 
#             print("*", end=" ")
#         else:
#             print(" ", end=" ")  
#     print()                   


# #hollow inverted pyramid pattern
# rows = int(input("Enter the row size for the pattern: "))
# for i in range(rows,0,-1 ):  # Outer loop for rows
#     for j in range(rows  - i):  # Inner loop for spaces
#         print(" ", end=" ")
#     for k in range(1, 2 * i):  # Inner loop for stars
#         if k == 1 or k == 2 * i - 1 or i == rows:  # Print star on borders
#             print("*", end=" ")
#         else:
#             print(" ", end=" ")  # Print space inside
#     print()

# #numbers
# rows = int(input("Enter the row size for the pattern:"))
# for i in range(1, rows + 1):  # Outer loop for rows
#     for j in range(1, i + 1):  # Inner loop for columns
#         print(j, end=" ")  # Print numbers
#     print()



#trytest
# for i in range(1,10,2):
#     print(i) 
# 
# list=[2,3,5,7]
# list2=[9,6] 
# print(list+list2)

