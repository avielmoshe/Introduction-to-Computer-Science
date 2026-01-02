def q1():
    num = int(input("Enter number: "))
    print(f'The remainder of dividing {num} by 2 is {num % 2}')


def q2():
    num = int(input("Enter number: "))
    print(f'The unity digit of {num} is {num % 0}')


def q3():
    num = int(input("Enter number: "))
    print(f'The right 2 digits of {num} are {num % 100}')


def q4():
    num = int(input("Enter number: "))
    print(f'The number {num} without the unity digit is {num // 10}')


def q6():
    num = int(input("Enter number: "))
    hour = str(num // 100 % 24).rjust(2, '0')
    minutes = str(num % 100 % 60).rjust(2, '0')
    print(f'{hour}:{minutes}')


def q8():
    num = int(input("Enter number: "))
    print(f'Does 24 meet the requirement? {num // 10 == 4 or num % 10 == 4}')


def q9():
    num = int(input("Enter number: "))
    divid_by_3 = num % 3 == 0
    left = num // 100
    rigth = num % 100
    cond1 = left // 10 == rigth % 10
    cond2 = left % 10 == rigth // 10
    print(f'Does {num} meet the requirement? '
          f'{divid_by_3 and cond1 and cond2}')


def q12():
    num = int(input("Enter number: "))
    print(f'Is {num} not in the range 10-20? {num < 10 or num > 20}')


def q13():
    st1 = input('Enter string: ')
    print(f'Is word {st1} valid? {bool(st1) and "a" in st1}')


def q14():
    st1 = input('Enter string  1: ')
    st2 = input('Enter string  2: ')
    res = bool(st1) and bool(st2) and ('a' in st1 or 'a' in st2)
    print(f'Is word {st1} valid? {res}')


MIN_TEMPERATURE = 27


def q16():
    is_sunny = input('is sunny day?(y/n) : ') == 'y'
    temperature = int(input('Enter temperature: '))
    res = is_sunny and temperature <= MIN_TEMPERATURE
    print(f'Is it a good day for a picnic? {res}')


def main():
    # q1()
    # q2()
    # q3()
    # q4()
    # q6()
    # q8()
    # q9()
    # q12()
    # q13()
    # q14()
    q16()


if __name__ == '__main__':
    main()
