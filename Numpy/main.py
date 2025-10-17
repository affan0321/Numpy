import numpy as np

# arr = np.arange(1,31).reshape(6,5)
# print(arr)

# print(arr[0:2,1:3])

# slice = arr[3:,3:]
# print(slice)



# arr = np.arange(11,21)
# print(arr)
# bool_index= arr%2 ==0
# print(bool_index)

# arr = arr[bool_index]
# print(arr)


#Arithmetic operations

# a1 = np.array([1,2,3,4,5,])
# a2 = np.array([6,7,8,9,10])

# a3 = a1 + a2

# print(a3)


# Shallow copy

# arr = np.arange(1,21)
# print(arr)
# slice = arr[:4]
# print(slice *10)


# Matrix operation

# A = np.array([[1,2],[3,4]])
# B = np.array([[5,6],[7,8]])

# C = A @ B

# print(C)



# Array Excercise

s = np.array([
    [5, 3, 4, 6, 7, 8, 9, 1, 2],
    [6, 7, 2, 1, 9, 5, 3, 4, 8],
    [1, 9, 8, 3, 4, 2, 5, 6, 7],
    
    [8, 5, 9, 7, 6, 1, 4, 2, 3],
    [4, 2, 6, 8, 5, 3, 7, 9, 1],
    [7, 1, 3, 9, 2, 4, 8, 5, 6],
    
    [9, 6, 1, 5, 3, 7, 2, 8, 4],
    [2, 8, 7, 4, 1, 9, 6, 3, 5],
    [3, 4, 5, 2, 8, 6, 1, 7, 9]
])

# b = np.sum(s,axis=1)

# for i in b:
#     if i != 45:
#         print("Sudoku is not valid!")
#         break
#     else:
#         print("Sudoku is valid!")

# d = np.sum(s[:3,:3])


# for i in range(0,9,3):
#     for j in range(0,9,3):
#         n = s[0:3,0:3]
#         print(n.sum())



# Columns: [Age, Math Marks, Science Marks]
data = np.array([
    [18, 85, 78],   # Student 1
    [19, 92, 88],   # Student 2
    [17, 76, 95],   # Student 3
    [18, 65, 70],   # Student 4
    [20, 90, 85]    # Student 5
])


# Get the shape of matrix

# data = data.shape
# print(data)


# Average age of students

# avg = np.mean(data[:,0])
# print(avg)

# math = data[:,1]
# print(math)

# max_sci_mark = np.max(data[:,2])
# print(max_sci_mark)



# Great90 = data[data[:,1]>90]
# print(Great90)



# plus5 = data[:,1] + 5
# print(plus5)

# age = len(data[data[:,0] < 19])
# print(age)



# marksmean = np.mean(data[:,1:],axis=0)
# print(marksmean) 

more80 = data[(data[:,1]>= 80) & (data[:,2] >= 80)]
print(more80)

