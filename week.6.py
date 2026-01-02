def q1():
    num = int(input("enter number: "))

    seq = range(1,num+1)
    i = 0
    while i < len(seq):
        print(seq[i] , end="")
        if i < len(seq)-1:
            print(", ", end="")
        i +=1

def q2():
    num = int(input("enter number: "))

    seq = range(num,0,-1)
    i = 0
    while i < len(seq):
        print(seq[i] , end="")
        if i < len(seq)-1:
            print(", ", end="")
        i +=1

def q3():
    str = input("enter your name: ")
    res = ""
    for i, ch in enumerate(str,1):
        if (ord(ch) + i) % 3 == 0:
            res += ch
    print(res)

def q4():
    num = int(input("enter number: "))
    res = ""

    for i in range(1, num + 1):
        temp = i
        is_boom = False

        if i % 7 == 0:
            is_boom = True

        if not is_boom:
            while i > 0:
                if i % 10 == 7:     
                    is_boom = True
                    break
                i = i // 10        

        if is_boom:
            res += "BOOM, "
        else:
            res += str(temp) + ", "

    print(res)

def q5():
    num = int(input("Enter the number"))
    res = 0
    multi = 1 

    while num > 0:
        x = num % 10
        x = x * x

        while x > 9:
            sum += x % 10 
            x = x // 10

        res += x * multi
        multi = multi * 10
        num = num // 10


    print(res)


def q5():
    num = int(input("Enter the number: "))
    res = 0
    multi = 1 

    while num > 0:
        digit = num % 10
        x = digit * digit   

        while x > 9:
            x = (x // 10) + (x % 10)

        res += x * multi
        multi *= 10
        num //= 10

    print(res)

def q6():
    count = 0

    for a in range(1, 10):          
        for b in range(1, 10):        
            if a >= b:              
                continue

            for num in range(10, 100):     
                for den in range(10, 100): 
                    if num >= den:
                        continue

                    num_tens = num // 10
                    den_ones = den % 10

                    if den_ones == 0:
                        continue

                    fake_num = num_tens
                    fake_den = den_ones

                    if fake_num == a and fake_den == b:
                        if num * fake_den == den * fake_num:
                            print(f"{a}/{b} == {num}/{den}")
                            count += 1

    print(count)


def q7():
    n1 = int(input("Enter first number: "))
    n2 = int(input("Enter second number: "))

    new_number = 0 
    multi = 1 

    while n1 > 0:
        count = n1 % 10     
        digit = n2 % 10    

        for i in range(count):
            new_number = new_number+digit*multi
            multi *= 10
            if multi > 100000000:
                break

        n1 //= 10
        n2 //= 10


    


def q8():
    num = int(input("Enter number: "))
    d = int(input("Enter digit length: "))

    result = 0
    multiplier = 1
    temp = num

    while temp > 0:
        block_val = 0
        count = 0  
        
        for i in range(d):
            if temp == 0:
                break
            
            digit = temp % 10

            block_val = block_val * 10 + digit
            temp //= 10
            count += 1
            

        result = block_val * multiplier + result
        

        for i in range(count):
            multiplier *= 10

    print(result)

def q9():
    num = int(input("Enter number: "))

    for i in range(num):

        for j in range(i):
            print(" ", end="")

        for k in range(num - i):
            print("* ", end="")
            

        print()

def q10():
    num = int(input("Enter number: "))

    for i in range(num):

        for j in range(i):
            print(" ", end="")

        for k in range(num - i):
            print("* ", end="")
            

        print()

    for i in range(num):

        for j in range(num - (i+1)):
            print(" ", end="")

        for k in range(i+1):
            print("* ", end="")
            

        print()

def q11():
    num = int(input("Enter number: "))
    for i in range(num): 
        for i in range(num):
            print("*" * num, end=" ")    
        print("\n")
        for i in range(num):
            print("*" * num, end=" ")                     
        print("\n")
        for i in range(num):
            print("*" * num, end=" ")                     
        print("\n")
        print("\n")
   
def q12():
    num = int(input("Enter number: "))

    row = ("*" * num + " ") * num  

    for _ in range(num):  
        for _ in range(num):  
            print(row)
        print()  


            



def main():
    # q1()

    # q2()
    # q3()
    # q4()
    # q5()
    # q6()
    # q7()
    # q8()
    # q9()
    # q10()
    # q11()
    q12()


main()