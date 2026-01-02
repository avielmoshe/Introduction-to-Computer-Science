def find_col_with_most_appearances(letters, ch):
    if not letters or not letters[0]:
        return -1

    num_cols = len(letters[0])
    counts = [0] * num_cols

    for row in letters:
        for col in range(num_cols):
            if row[col] == ch:
                counts[col] += 1

    max_count = max(counts)
    if max_count == 0:
        return -1

    return counts.index(max_count)

def q1():
    letters = [
        ['a', 'b', 'c'],
        ['d', 'a', 'c'],
        ['a', 'b', 'a']
    ]    
    print(find_col_with_most_appearances(letters,"d"))

def max_on_edge(numbers):
    rows = len(numbers)
    cols = len(numbers[0])

    max_val = numbers[0][0]

    for i in range(cols):
        if numbers[0][i] > max_val:
            max_val = numbers[0][i] 
        
        if numbers[rows - 1][i] > max_val:
            max_val = numbers[rows - 1][i] 

    for i in range(rows):
        if numbers[i][0] > max_val:
            max_val = numbers[i][0] 

        if numbers[i][cols-1] > max_val:
            max_val = numbers[i][0] 

    return max_val

def q2():
    numbers = [
    [1, 2, 3],
    [4, 5, 6],
    [10, 8, 11]
    ]
    print(f'the matrix is {numbers} and the max value on the edage is {max_on_edge(numbers)}')

def create_snake(rows, cols):
    matrix = [[0 for _ in range(cols)] for _ in range(rows)]
    current = 1 
    is_up = False
    for col in range(cols-1,-1,-1):
        if not is_up:
            for row in range(rows - 1, -1, -1):
                matrix[row][col] = current
                current +=1
        else:
            for row in range(rows):
                matrix[row][col] = current
                current +=1

        is_up = not is_up
    return matrix

def q3():
    print(create_snake(3,2))

def q4():
    pass



def main():
    # q1()
    # q2()
    q3()
    # q4()



if __name__ == "__main__":
    main()