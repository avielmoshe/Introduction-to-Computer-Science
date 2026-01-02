def q1():
    coefficient_a = float(input("enter the coefficient of x: "))
    coefficient_b = float(input("enter the coefficient of b: "))


    if coefficient_a ==0 and coefficient_b != 0:
        print("No Solution")
    elif coefficient_a == 0 and coefficient_b == 0:
        print("Infinite solutions")
    else:
        num_x = -coefficient_b / coefficient_a
        print(f'x = {num_x}')

def q2():
    type_of_relationship  = input("Enter relationship (family/close/other): ")
    years_of_acquaintance = int(input("Enter years of acquaintance: "))
    travel_time = float(input("Enter travel time in hours: "))


    if type_of_relationship == "family":
        gift_amount = 1000
    elif type_of_relationship == "close":
        gift_amount = 500
    else:
        gift_amount = 250

    if years_of_acquaintance > 3 and type_of_relationship != "family":
        gift_amount += 50

    if travel_time > 1 and type_of_relationship != "family":
        gift_amount -= 50 

    print(f"Recommended gift amount: {gift_amount} NIS")

def q3():
    subscription_type = input("Enter subscription type (adult/child): ")
    books_borrowed = int(input("Enter number of books already borrowed: "))
    has_overdue = input("Is there a book held for more than a month? (yes/no): ")

    has_overdue = has_overdue.lower() == "yes"

    if subscription_type == "adult":
        limit = 5
    else:
        limit = 3

    if has_overdue:
        can_borrow = False
    else:
        can_borrow = books_borrowed < limit

    print(can_borrow)

def q4():
    bagrut_average = float(input("Enter your bagrut averge from school: "))
    psychometric_score = float(input("Enter your psychometric grade: "))
    quantitative_score = float(input("Enter your quantitative score: "))
    english_score = float(input("Enter your english score: "))

    combined_score = psychometric_score * 0.8 + (bagrut_average / 1.2)

    res = False

    if bagrut_average >= 102:
        res = True

    if psychometric_score >= 700 and quantitative_score >= 145 and  english_score >= 120:
        res = True

    if combined_score >= 600:
        res = True

    print(res)
    
def q5():
    resting_heart_rate = int(input("Enter your resting heart rate: "))
    weeks_trained = int(input("Enter the number of weeks that you already trained: "))

    if weeks_trained <= 2 or resting_heart_rate > 70:
        recommended_distance_km = 3
    elif weeks_trained <= 4:
        recommended_distance_km = 5
    elif resting_heart_rate<60:
        recommended_distance_km = 10
    else:
        recommended_distance_km = 8

    print(recommended_distance_km)

def q6():
    exam_score = int(input("Enter exam score: "))
    homework_avg = int(input("Enter homework averge: "))
    homework_submitted = int(input("Enter the number of homework that submitted (0-8)"))

    final_score = 0  

    if homework_submitted <= 4:
        final_score = 0
    elif homework_submitted in [5, 6]:
        if exam_score >= 55:
            final_score = exam_score * 0.8 + homework_avg * 0.2
        else:
            final_score = exam_score
    elif homework_submitted in [7, 8]:
        if exam_score <= 54:
            if homework_avg >= 80:
                final_score = max(exam_score, exam_score * 0.75 + homework_avg * 0.25)
            else:
                final_score = max(exam_score, exam_score * 0.8 + homework_avg * 0.2)
        else:
            final_score = max(exam_score, exam_score * 0.7 + homework_avg * 0.3)

    print(f"the final grade is: {final_score}")

def main():
    # q1()
    # q2()
    # q3()
    # q4()
    # q5()
    q6()


main()