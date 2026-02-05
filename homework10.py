def is_switched_number(number):
    if number < 10:
        return True

    last_digit = number % 10
    prev_digit = (number // 10) % 10

    if (last_digit % 2) == (prev_digit % 2):
        return False
    return is_switched_number(number // 10)

def q1():
    print(is_switched_number(1873))

def has_switched_couple(number):
    if number < 10:
        return False

    last_digit = number % 10
    prev_digit = (number // 10) % 10

    if (last_digit % 2) != (prev_digit % 2):
        return True

    return has_switched_couple(number // 10)

def q2():
        print(has_switched_couple(1873))

def switch_values(the_list, index_begin, index_end):
    if index_begin >= index_end:
        return

    the_list[index_begin], the_list[index_end] = \
          the_list[index_end], the_list[index_begin]

    switch_values(the_list, index_begin + 1, index_end - 1)

def q3():
    list = [10,20,30,40,50]
    switch_values(list,0,4)
    print(list)

def has_sequence(the_list, num, index=0, expected=1):
    if expected > num:
        return True

    # סוף הרשימה – אין רצף
    if index == len(the_list):
        return False

    current = the_list[index]

    # אם הערך מתאים למה שמצפים לו
    if current == expected:
        return has_sequence(the_list, num, index + 1, expected + 1)

    # אם חיפשנו 1 ונכשלנו – ממשיכים לחפש
    if expected == 1:
        return has_sequence(the_list, num, index + 1, 1)

    # אם הרצף נשבר אבל הערך הוא 1 – התחלה חדשה
    if current == 1:
        print(5)
        return has_sequence(the_list, num, index + 1, 2)


    # אחרת – הרצף נשבר, חוזרים לחפש 1
    return has_sequence(the_list, num, index + 1, 1)


def q4():
    print(has_sequence([3,8,2,6,5,1,2,3],2))

def q5():
    pass

def q6():
    pass

def main():
    # q1()
    # q2()
    # q3()
    q4()
    q5()
    q6()

if __name__ == "__main__":
    main()