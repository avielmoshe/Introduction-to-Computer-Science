def q1():
    None


# def super_function(*args, **ks):
#     print("Positional args:", args)
#     print("Keyword args:", ks)

# super_function(1, 2, 3, 4, color="red", speed="fast" ,level=5)

def factorial_fun(num):
    total = 1
    for i in range(num-1):
        total *= num
        num -=1
    return total    

def q7():
    factorial = factorial_fun(5)
    print(factorial)

def fibo(index):
    a_n, a_n1 = 1, 1
    for i in range(1,index):
        a_n,a_n1 = a_n1,a_n + a_n1
    return a_n1

def make_new_number(num_1,num_2):
    new_number = 0
    multi = 1
    while num_1>0 and num_2>0:
       digit_1 = num_1 % 10 
       digit_2 = num_2 % 10 
       smaller_digit = digit_2 if digit_1 > digit_2 else digit_1
       new_number += smaller_digit * multi
       multi *= 10 
       num_1, num_2 = num_1 // 10, num_2 // 10

    if not num_1 and not num_2:  
        return new_number
    else:
        return  -1 

def to_binary(x,base):
    result = 0
    factor = 1

    if x == 0:
        return 0

    while x > 0:
        digit = x % base     
        result += digit * factor
        factor *= 10           
        x //= base

    return result


def q8():
    index = int(input("Enter the index : "))
    fibo_number = fibo(index)
    print(f"phibonacci item in index {index} = {fibo_number}")

def q11():
    num_1 = int(input("enter number: "))
    num_2 = int(input("enter number: "))
    new_number = make_new_number(num_1,num_2)
    print(new_number)

def q13():
    number = int(input("Enter number that you wish to convert to binary : "))
    base = int(input("Enter in which base: "))
    binary_number = to_binary(number,base)   
    print(binary_number) 
    
def main():

    # q7()
    # q8()
    # q11()
    q13()


main()