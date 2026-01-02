def is_mirror_pair(a, b):
    if a <= 0 or b <= 0:
        return False

    count_a = 0
    temp = a
    while temp > 0:
        count_a += 1
        temp //= 10

    count_b = 0
    temp = b
    while temp > 0:
        count_b += 1
        temp //= 10

    if count_a != count_b:
        return False

    reversed_a = 0
    temp = a
    while temp > 0:
        reversed_a = reversed_a * 10 + temp % 10
        temp //= 10

    return reversed_a == b


def is_mirror_list(numbers):
    n = len(numbers)

    for i in range(n // 2 + n % 2):
        if not is_mirror_pair(numbers[i], numbers[n - 1 - i]):
            return False

    return True

def draw_histogram(numbers):
    if len(numbers) == 0:
        return

    max_value = max(numbers)

    for level in range(max_value, 0, -1):
        for i in range(len(numbers)):
            if numbers[i] >= level:
                print("*", end="")
            else:
                print(" ", end="")

            if i != len(numbers) - 1:
                print("  ", end="")  
        print()

    for i in range(len(numbers)):
        print(numbers[i], end="")
        if i != len(numbers) - 1:
            print("  ", end="")
    print()

def long_sum(list1, list2):
    result = []
    carry = 0

    i1 = len(list1) - 1
    i2 = len(list2) - 1

    while i1 >= 0 or i2 >= 0:
        digit1 = list1[i1] if i1 >= 0 else 0
        digit2 = list2[i2] if i2 >= 0 else 0

        total = digit1 + digit2 + carry
        result.insert(0, total % 10)  # מוסיפים בהתחלה
        carry = total // 10

        i1 -= 1
        i2 -= 1

    if carry > 0:
        result.insert(0, carry)

    return result


def q3():
    print(long_sum([4, 3, 2, 1], [7, 9]))        # [1, 3, 3, 1]

def q2():
    draw_histogram([2,10,6,8])

def q1():
    print(is_mirror_list([321, 121, 54, 45, 121, 123]))    


def main():
    # q1()
    # q2()
    q3()

main()
