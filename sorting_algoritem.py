def sort_numbers_optimization(numbers):
    for i in range(len(numbers)-1,0,-1):
        has_changed = False
        for j in range(i):
            if numbers[j]>numbers[j+1]:
                numbers[j],numbers[j+1]=numbers[j+1],numbers[j]
                has_changed = True
        if not has_changed:
            return

def q1():
    l1 = [1,8,3,9,10,5,2,4]
    sort_numbers_optimization(l1)
    print(l1)

def sort_numbers_Insertion(numbers):
    for i in range(1, len(numbers)):
        for j in range(i, 0, -1):
            if numbers[j - 1] < numbers[j]:
                break
            numbers[j], numbers[j - 1] = numbers[j - 1], numbers[j]

def q2():
    l1 = [1,8,3,9,10,5,2,4]
    sort_numbers_Insertion(l1)
    print(l1)
 
def sort_numbers(numbers):
    indexes_list = [0] * (max(numbers) + 1)
    for num in numbers:
        indexes_list[num] += 1
        index = 0
        for i in range(len(indexes_list)):
            for _ in range(indexes_list[i]):
                numbers[index] = i
                index += 1

def q3():
    l2 = [1,8,3,1,8,10,11,12,9,9,9,9,10,5,2,4]
    sort_numbers_Insertion(l2)
    print(l2)

def binary_search(numbers, start, end, num):
    while start <= end:
        middle = (start + end) // 2
        if num == numbers[middle]:
            return middle
        if num < numbers[middle]:
            end = middle - 1
        else:
            start = middle + 1
    return -1

def q4():
    numbers, num = [1, 2, 7, 12, 15, 24, 32, 45, 81], 24
    index = binary_search(numbers, 0, len(numbers) - 1, num)
    if index == -1:
        print(f'{num} not found')
    else:
        print(f'{num} found in index: {index}')

def main():
    # q1()
    # q2()
    # q3()
    q4()




if __name__ == "__main__":
    main()