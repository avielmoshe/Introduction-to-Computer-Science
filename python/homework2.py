

def q1():
    date_not_org = int(input("Enter your date in this order ddMMyyyy: "))
    year  = date_not_org % 10000
    month = date_not_org % 1000000 // 10000
    day   = date_not_org % 100000000 // 1000000

    print(f"The date is {day}/{month}/{year}")

def q2():
    num         = int(input("Enter 3 digit number: "))
    right_num   = num % 10 
    middle_num  = num % 100 // 10
    left_num    = num // 100

    print(right_num/2==left_num+middle_num) 

def q3():
    num         = int(input("Enter 4 digit number: "))

    right_num         = num % 10 
    middle_right_num  = num % 100 // 10
    middle_left_num   = num % 1000 // 100
    left_num          = num // 1000

    is_middle = middle_right_num==middle_left_num

    print(is_middle and right_num-1 == left_num) 

def main():
    # q1()
    # q2()
    q3()
    pass


main()