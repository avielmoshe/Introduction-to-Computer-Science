def count_even_digits(n):
    if n == 0:
        return 0

    last_digit = n % 10
    if last_digit % 2 == 0:
        return 1 + count_even_digits(n // 10)
    else:
        return count_even_digits(n // 10)

def q1():
    num = 12
    print(count_even_digits(num))

def cal_factorial(n):
    if n <= 1:
        return 1
    return n * cal_factorial(n-1)

def q2():
    num =5
    print(cal_factorial(num))

def sum_list(lst, i=0):
    if i == len(lst):    
        return 0
    
    return lst[i] + sum_list(lst, i + 1)

def q3():
    list = [1,2,3,4,5,6]
    print(sum_list(list))

def remainder_is(num , module):
    if num < module:
        return num
    
    return remainder_is(num-module,module)

def q4():
    print(remainder_is(3,3))

def num_to_string(num):
    if num == 0:
        return ""
    
    digit = num % 10 
    ch = chr(ord('A')+digit)
    return num_to_string(num // 10) + ch

def q5():
    print(num_to_string(12345))


def main():
    # q1()
    # q2()
    # q3()
    # q4()
    q5()




if __name__ == "__main__":
    main()