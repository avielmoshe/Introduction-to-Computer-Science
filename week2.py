
def q9():
    num = int(input("enter number with 4 digit"))
    res = num % 3 == 0
    left_side = num // 100 
    right_side = num % 100

    cond1 = left_side // 10 == right_side % 10 
    cond2 = left_side % 10 == right_side // 10
    print(f"Does {num} meet the requirement? {res and cond1 and cond2 }") 

    
def q10():
    first_num   = int(input("enter the first number:"))
    seconed_num = int(input("enter the seconed number:"))

    res = first_num / seconed_num
    res = int(res*100)/100

    print(res)

def q11():
    num = int(input("enter number:"))
    res = num % 2 == 0 or num < 0

    print(f"Dose {num} meet the requirement ? {res}")

def q12():
    num = int(input("enter number:"))
    is_num_in_range = 10 >= num or 20 <= num

    print(f"Is {num} not in the range 10-20? {is_num_in_range}")

def q13():
    word = input("enter your word:")
    is_empty = bool(word)
    is_a_in_word = "a" in word
    res = is_empty and is_a_in_word

    print(f"Is word {word} valid? {res}")

def main():
    # q9()
    # q10()
    # q11()
    # q12()
    q13()

main()