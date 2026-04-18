def q1():
    # הגדרת הרשימה
    lst = [-42, 94, -12, 9, 47, 99, 12, 19, -5, 7, 39, 2]
##SAdadsad
    # a) אורך הרשימה
    print(len(lst))

    # b) סכום האיברים מאינדקס 2 ועד סוף הרשימה
    print(sum(lst[2:]))

    # c) המספר המקסימלי והאינדקס שלו
    max_value = max(lst)
    max_index = lst.index(max_value)
    print("מקסימום:", max_value)
    print("אינדקס:", max_index)

    # d) ממוצע המספרים ברשימה
    print(sum(lst) / len(lst))

    # e) הוספת סכום הרשימה לסוף הרשימה
    lst.append(sum(lst))
    print(lst)

    # f) הדפסת הרשימה בסדר הפוך
    print(lst[::-1])

def sum_2d_list(matrix):
    total = 0
    for row in matrix:
        for value in row:
            total += value
    return total

def min_max_2d_list(matrix):
    min_val = matrix[0][0]
    max_val = matrix[0][0]

    for row in matrix:
        for value in row:
            if value < min_val:
                min_val = value
            if value > max_val:
                max_val = value

    return min_val, max_val

def sum_above_diagonal(matrix):
    n = len(matrix)
    total = 0
    for i in range(n-1):          # שורה אחרונה לא מכילה איברים מעל האלכסון
        for j in range(i+1, i+2):   # j > i
            total += matrix[i][j]
    return total

def column_with_most(matrix, number):
    if not matrix:
        return -1
    
    max_cols = max(len(row) for row in matrix)
    counts = [0] * max_cols  

    for col in range(max_cols):
        for row in matrix:
            if col < len(row) and row[col] == number:
                counts[col] += 1

    if max(counts) == 0:
        return -1

    return counts.index(max(counts))





def q6():
    matrix = [
    [10, 35, 20],
    [35, 35],
    [5, 35, 35, 35]
    ]

    print(column_with_most(matrix, 35))  

def q5():
    matrix = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
    ] 
    total = sum_above_diagonal(matrix)
    print(total)

def q4():
    matrix = [
        [1,2,3],
        [4,5,6],
        [7,8,9]
    ]
    mini,max = min_max_2d_list(matrix)
    print(mini,max)

def q3():
    matrix = [
        [1,2,3],
        [4,5,6],
        [7,8,9]
    ]
    total = sum_2d_list(matrix)
    print(total)

def main():
    # q1()
    # q3()
    # q4()
    # q5()
    q6()

main()
