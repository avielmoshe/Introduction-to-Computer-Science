import numpy as np

def gaussian_elimination(augmented_matrix):
    # הופכים את המערך ל-float כדי שנוכל לחלק עשרונית בלי לאבד מידע
    A = np.array(augmented_matrix, dtype=float)
    rows, cols = A.shape
    num_vars = cols - 1  # העמודה האחרונה היא וקטור התוצאות (b)

    # שלב 1: דירוג המטריצה (משולש עליון)
    for i in range(min(rows, num_vars)):
        # אם האיבר המוביל (פיבוט) הוא 0, צריך להחליף שורות
        if np.isclose(A[i, i], 0):
            for k in range(i + 1, rows):
                if not np.isclose(A[k, i], 0):
                    A[[i, k]] = A[[k, i]]  # פעולת שורה: החלפת שורות
                    break
            else:
                continue  # אם לא מצאנו, זה אומר שיש משתנה חופשי (נעבור לעמודה הבאה)

        # איפוס כל האיברים שמתחת לפיבוט
        for j in range(i + 1, rows):
            factor = A[j, i] / A[i, i]
            A[j] = A[j] - factor * A[i]  # פעולת שורה: R_j = R_j - c*R_i

    # שלב 2: בדיקת סוג הפתרון
    # א' - אין פתרון (שורת אפסים ששווה למספר שונה מאפס)
    for i in range(rows):
        # בודקים אם כל המקדמים בעמודות המשתנים הם 0, אבל התוצאה לא 0
        if np.all(np.isclose(A[i, :-1], 0)) and not np.isclose(A[i, -1], 0):
            return "אין פתרון (המערכת סתירתית)"

    # ב' - אינסוף פתרונות (מספר הפיבוטים/השורות שאינן אפס קטן ממספר המשתנים)
    # נספור מהי הדרגה (Rank) של המטריצה
    rank = 0
    for i in range(rows):
        if not np.all(np.isclose(A[i, :-1], 0)):
            rank += 1
            
    if rank < num_vars:
        return f"אינסוף פתרונות (יש {num_vars - rank} משתנים חופשיים)"

    # ג' - פתרון יחיד (הדרגה שווה למספר המשתנים)
    # שלב 3: הצבה אחורנית
    solution = np.zeros(num_vars)
    for i in range(num_vars - 1, -1, -1):
        # מבודדים את המשתנה: מעבירים אגפים ומחלקים בפיבוט
        solution[i] = (A[i, -1] - np.dot(A[i, :-1], solution)) / A[i, i]
        
    return f"פתרון יחיד: {solution}"

# ---- דוגמאות להרצה ----

# מקרה 1: פתרון יחיד
# x + 2y = 5
# 3x + 4y = 11
matrix_unique = [
    [1, 2, 5],
    [3, 4, 11]
]

# מקרה 2: אינסוף פתרונות
# x + y = 3
# 2x + 2y = 6
matrix_infinite = [
    [1, 1, 3],
    [2, 2, 6]
]

# מקרה 3: אין פתרון
# x + y = 3
# x + y = 4
matrix_no_solution = [
    [1, 1, 3],
    [1, 1, 4]
]

print(gaussian_elimination(matrix_unique))
print(gaussian_elimination(matrix_infinite))
print(gaussian_elimination(matrix_no_solution))