def q1():
    num = int(input("Enter a positive number up to 20: "))

    if 1 <= num <= 20:
        i = 1
        result = ""
        while i <= num:
            result += str(i) + " "
            i += 1
        print(result)
    else:
        print("Number must be between 1 and 20")

def q4():
    num = int(input("Enter a positive number up to 100: "))

    if 1 <= num <= 100:
        i = 0
        sum_of_even_num = 0
        while i <= num:
            if i % 2 == 0:
                sum_of_even_num += i
            i += 1 
        print(sum_of_even_num)
    else:
        print("Number must be between 1 and 100")

def q5():
    num = int(input("Enter a positive number (0 to stop): "))

    total = 0

    while num != 0:
        total += num
        num = int(input("Enter a positive number (0 to stop): "))

    print("The sum of the numbers is", total)

def q6():
    num = int(input("Enter a positive integer: "))

    temp = num
    count = 0

    while temp > 0:
        temp //= 10      # remove last digit
        count += 1

    print("The number", num, "has", count, "digits.")

def q7():
    num = int(input("Enter a positive integer: "))

    sum ,temp= 0,num
    while temp > 0:
        digit = temp % 10
        sum += digit
        temp //= 10
    print("Sum of the digits of", num, "is", sum)

def q8():
    num = int(input("Enter a positive integer: "))

    temp = num
    sum_even = 0

    while temp > 0:
        digit = temp % 10      # take last digit
        if digit % 2 == 0:     # check if even
            sum_even += digit
        temp //= 10            # remove last digit

    print("Sum of even digits of", num, "is", sum_even)

def q9():
    num = int(input("Enter a positive number up to 10: "))

    if 1 <= num <= 10:
        row = 1
        result = ""
        while row <= num:
            result += ' * ' * num + '\n'
            row += 1
        print(result)
    else:
        print("Number must be between 1 and 10")

def q10():
    num = int(input("Enter a positive number up to 10: "))

    if 1 <= num <= 10:
        row = 1
        result = ""
        while row <= num:
            result += ' ' * (num - row) + '* ' * row + '\n'
            row += 1
        print(result)
    else:
        print("Number must be between 1 and 10")

def q11():
    word = input("enter your word with some capital letters: ")

    index = len(word) - 1
    result = ""
    while index >= 0:
        if 'A' <= word[index] <= 'Z':
            result += word[index]
        index -= 1

    print(result)

def q12():
    word = input("enter your words: ")
    letter = input("enter the letter that you want to count: ")

    index = len(word)-1
    count = 0
    while index >= 0:
        if word[index] == letter:
            count += 1
        index -= 1
    
        
    print(f'in the word{word} the letter {letter} ex {count} times')

def q13():
    num = int(input("Enter a positive integer: "))
    num_to_count = int(input("Enter the digit you want to count: "))

    counter = 0

    while num > 0:
        digit = num % 10
        if num_to_count == digit:
            counter += 1
        num = num // 10

    print("The digit", num_to_count, "appears", counter, "times.")

def q14():
    num = int(input("Enter a positive integer: "))

    pos = 0            
    new_number = 0     
    multiplier = 1      

    temp = num
    while temp > 0:
        digit = temp % 10

        if pos % 2 == 0:   
            new_number = digit * multiplier + new_number
            multiplier *= 10

        temp //= 10
        pos += 1

    print(new_number)


def q15():
    num_1 = int(input("Enter a positive integer: "))
    num_2 = int(input("Enter a positive integer: "))

    counter = 0

    while num_1 > 0:
        digit_1 = num_1 % 10
        digit_2 = num_2 % 10
        if digit_1 == digit_2:
            counter += 1
        num_1 = num_1 // 10 
        num_2 = num_2 // 10 
    print(counter)

def q16():
    id_number = int(input("Enter your ID number (9 digits): "))

    pos = 9           
    sum_of_numbers = 0     
    verification_digit = 0
    temp = id_number

    while pos > 0:
        digit = temp % 10

        if pos == 9:
            verification_digit = digit
            pos -= 1
            temp //= 10
            continue
        if pos % 2 == 0:   
            sum_of_multiplier = digit * 2
            sum_of_numbers += sum_of_multiplier % 10 + sum_of_multiplier // 10
        else:
            sum_of_numbers += digit


        temp //= 10
        pos -= 1

    next_multiple_of_10 = ((sum_of_numbers // 10) + 1) * 10

    is_verification_digit = next_multiple_of_10-sum_of_numbers == verification_digit
    print(is_verification_digit)

def q17():
    num = int(input("Enter a positive integer: "))

    new_number = 0
    multiplier = 1  

    temp = num

    while temp > 9:   
        d1 = temp % 10         
        d2 = (temp // 10) % 10  

        new_number += (d1 * 10 + d2) * multiplier

        temp //= 100
        multiplier *= 100

    if temp > 0:
        new_number += temp * multiplier

    print(new_number)

def q18():
    num = int(input("Enter a positive integer: "))

    temp = num
    reverse = 0
    digits = 0

    while temp > 0:
        last = temp % 10
        reverse = reverse * 10 + last
        temp //= 10
        digits += 1

    result = num * (10 ** digits) + reverse

    print(result)

def q19():
    while True:
        a = int(input("Enter first number: "))
        op = input("Enter sign (+ or -): ")
        b = int(input("Enter second number: "))
            
        if op == '-':
            print("\n🔚 '-' sign detected, ending the program.")
            break  
        elif op == '+':
            if a < b:
                print("\n❗ As per the exercise instruction, the first number (a) must be greater than the second (b). Try again.")
                continue
            sum_result = a + b
            diff_result = a - b

            temp = sum_result
            multiplier = 1
            
            while temp > 0:
                temp //= 10 
                multiplier *= 10 
            

            final_number = diff_result * multiplier + sum_result
            

            print(f"The expression {a}{op}{b} = {final_number}\n")
        else:
            print("\n❌ Invalid sign. Please enter only '+' or '-'.")





def main():
    # q1()
    # q4()
    # q5()
    # q6()
    # q7()
    # q8()
    # q9()
    # q10()
    # q11()
    # q12()
    # q13()
    # q14()
    # q15()
    # q16()
    # q18()
    q19()

main()