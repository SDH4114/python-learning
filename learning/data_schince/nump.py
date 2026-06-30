import numpy as np

# это масив
arr = np.array([1, 2, 3, 4, 5, 6])

# это трехмерный масив матрица
matrix1 = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

# это трехмерный масив матрица
matrix2 = np.array([[5, 8, 3], [8, 2, 4], [9, 1, 6]])

megamatrix = matrix1 * matrix2

print(arr * 2)
print(f"{matrix1}*{matrix2} = {megamatrix}")


# zeros - 0
zeros = np.zeros((3, 4))

print(zeros)
# [[0. 0. 0. 0.]
#  [0. 0. 0. 0.]
#  [0. 0. 0. 0.]]


# ones - 1
ones = np.ones((4, 3))

print(ones)
# [[1. 1. 1.]
#  [1. 1. 1.]
#  [1. 1. 1.]
#  [1. 1. 1.]]


linspace = np.linspace(0, 10, 5)
print(linspace)
# [ 0.   2.5  5.   7.5 10. ]

arange = np.arange(0, 10, 2)  # 0 - 10  это от какого до какого числа
# 2 это промежутки
print(arange)
# [0 2 4 6 8]


print(arr[1:4])
# [2,3,4]
print()


matrix1 = np.array(
    [
        [1, 2, 3, 7, 3, 8],  # 0
        [4, 5, 6, 1, 2, 9],  # 1
        [7, 8, 9, 4, 6, 0],  # 2
        [5, 7, 9, 2, 5, 1],  # 3
        [9, 6, 2, 1, 6, 4],  # 4
        [7, 9, 4, 6, 2, 3],  # 5
    ]
)


print(matrix1[1:5, :4])  # 1:5 отвечает за линии выйдет 1 2 3 4
# :4 выводит все до 5 символа  4 5 6 1
# [[4 5 6 1]
#  [7 8 9 4]
#  [5 7 9 2]
#  [9 6 2 1]]


are = np.arange(1, 13)
print(are)
# [ 1  2  3  4  5  6  7  8  9 10 11 12]

reshape = are.reshape((3, 4))  # мы из одно слойного масива делаем много слоынй
# 3 - сколько будет слоев , 4 по сколько штук (если больше возможного ошибка)
print(reshape)
# [[ 1  2  3  4]
#  [ 5  6  7  8]
#  [ 9 10 11 12]]

# del are , arr , matrix1 , matrix2 , megamatrix, reshape

arr1 = np.array([1, 3, 5])
arr2 = np.array([2, 4, 6])

# обьеденение в слои
stack = np.stack((arr1, arr2))
print(stack)
# [[1 3 5]
#  [2 4 6]]

vstack = np.vstack((arr1, arr2))
print(vstack)
# [[1 3 5]
#  [2 4 6]]


# обьеденение по горизонтали
hstack = np.hstack((arr1, arr2))
print(hstack)  # [1 3 5 2 4 6]


matrix1 = np.array(
    [
        [1, 2, 3, 7, 3, 8],  # 0
        [4, 5, 6, 1, 2, 9],  # 1
        [7, 8, 9, 4, 6, 0],  # 2
        [5, 7, 9, 2, 5, 1],  # 3
        [9, 6, 2, 1, 6, 4],  # 4
        [7, 9, 4, 6, 2, 3],  # 5
    ]
)

# делит матрицу по вертикали
split = np.split(matrix1, 2)
print(split)

print()

hsplit = np.hsplit(matrix1, 2)
print(hsplit)
# [array([[1, 2, 3],
#        [4, 5, 6],
#        [7, 8, 9],
#        [5, 7, 9],
#        [9, 6, 2],
#        [7, 9, 4]]),
# array([[7, 3, 8],
#        [1, 2, 9],
#        [4, 6, 0],
#        [2, 5, 1],
#        [1, 6, 4],
#        [6, 2, 3]])]

# делит матрицу по горизонтали
vsplit = np.vsplit(matrix1, 2)
print(vsplit)
# [array([[1, 2, 3, 7, 3, 8],
#        [4, 5, 6, 1, 2, 9],
#        [7, 8, 9, 4, 6, 0]]),
# array([[5, 7, 9, 2, 5, 1],
#        [9, 6, 2, 1, 6, 4],
#        [7, 9, 4, 6, 2, 3]])]

print("")

funcs = np.array([5, 2, 1, 4, 3])

print(np.mean(funcs))  # среднее арефметическое
print(np.std(funcs))  # Стандартное отклонение отностительно среднего арефметического
print(np.median(funcs))  # медиана
print(f"min - {np.min(funcs)}, max - {np.max(funcs)}")  # мнимум и максимум в масиве


salaries = np.array([30, 56, 34, 89, 36, 66, 87, 34, 53, 83, 93, 65, 82])

mean = np.mean(salaries)
std = np.std(salaries)
median = np.median(salaries)


print(f"Средния зарпалата - {mean}")
print(f"Средние отклонение от зарплаты - {std}")
print(f"медиана зарплат - {median}")

print(f"""минимальная зарплата - {np.min(salaries)},
максимальная зарплата - {np.max(salaries)}
""")

more_mean = salaries[salaries > mean]
# for salary in salaries:
#     if salary > mean:
#         more_mean.append(salary)
print(f"Больше средней зарплаты - {more_mean}")
