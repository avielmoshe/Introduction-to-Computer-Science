def q1():
    d1 = {
        'Amir': 21,
        'Gal': 18,
        'Noa': 25
    }
    d2 = dict(Amir = 21,Gal=18,Noa=25)
    print(d1)
    print(d2)
    

def print_dict_values(d1, l1):
    for name in l1:
        if d1.get(name):
            print(f"{name}:{d1.get(name)}")


def q2():
    d1 = {
        'Amir': 21,
        'Gal': 18,
        'Noa': 25
    }
    l1 = ['Amir', 'Yael', 'Gal', 'Noa', 'Shaked']
    print_dict_values(d1, l1)


def update_dict_ages(d1, l1):
    for name in l1:
        # if d1.get(name):
        #     d1[name] +=1
        # else:
        #     d1[name] = d1.get(name,18)
        d1[name] = d1.get(name , 17) + 1
    

def q3():
    d1 = {
        'Amir': 21,
        'Gal': 18,
        'Noa': 25
    }
    l1 = ['Amir', 'Yael', 'Gal', 'Noa', 'Shaked']
    update_dict_ages(d1, l1)
    print(d1)


def get_average(d1):
    sum = 0
    for name in d1:
        sum += d1.get(name)
    return sum/len(d1)



def q4():
    d1 = {
        'Amir': 21,
        'Gal': 18,
        'Noa': 25
    }
    res = get_average(d1)
    print(f'average is {round(res, 2)}')


def get_above_21(d1):
    names_above_21 = []
    for name in d1:
        if d1.get(name) >= 21:
            names_above_21.append(name)
    return names_above_21

def q5():
    d1 = {
        'Amir': 21,
        'Gal': 18,
        'Noa': 25
    }
    res = get_above_21(d1)
    print(f'Names above 21 are {res}')


def get_name_len_over_3(d1):
    names_above_3 = []
    for name in d1:
        if len(name) >= 3:
            names_above_3.append(name)
    return names_above_3


def q6():
    d1 = {
        'Amir': 21,
        'Gal': 18,
        'Noa': 25
    }
    res = get_name_len_over_3(d1)
    print(f'Names length over 3 are {res}')


def filter_dict_by_age(d1, filter_age):
    out = [name for name,age in d1.items() if age < filter_age]
    for name in out:
        d1.pop(name)
           
    
def q7():
    d1 = {
        'Amir': 21,
        'Gal': 18,
        'Noa': 25
    }
    filter_age = 25
    filter_dict_by_age(d1, filter_age)
    print(d1)


def get_history_value(d1):
    return d1["class"]["student"]["marks"]["history"]


def q8a():
    print('\nquestion 8a')
    sample_dict = {
        "class": {
            "student": {
                "name": "Mike",
                "marks": {
                    "physics": 70,
                    "history": 80
                }
            }
        }
    }
    print('value of history is', get_history_value(sample_dict))


def get_value(d1, k):
    pass


def q8b():
    print('\nquestion 8b')
    sample_dict = {
        "class": {
            "student": {
                "name": "Mike",
                "marks": {
                    "physics": 70,
                    "history": 80
                }
            }
        }
    }
    # implement recursive function for any key
    key = 'history'
    print('value of', key, 'is', get_value(sample_dict, key))
    key = 'marks'
    print('value of', key, 'is', get_value(sample_dict, key))
    key = 'stam'
    print('value of', key, 'is', get_value(sample_dict, key))


def create_dict(s1):
    d = {}
    for ch in s1:
        d[ch] = d.get(ch, 0) + 1
    return d


def q9():
    s1 = 'abd fba'
    d1 = create_dict(s1)
    print(d1)


def rename_key(d, from_key, to_key):
    d[to_key] = d.pop(from_key)
    return d

def q10():
    sample_dict = {
        "name": "Kelly",
        "age": 25,
        "salary": 8000,
        "city": "New york"
    }
    print(rename_key(sample_dict, 'city', 'location'))


def get_min(d1):
    min_sub, min_grade = None, None
    for sub, grade in d1.items():
        if min_grade is None or grade < min_grade:
            min_sub, min_grade = sub, grade
    return min_sub, min_grade



def q11():
    sample_dict = {
        'Physics': 82,
        'Math': 65,
        'history': 75
    }
    print(get_min(sample_dict))


def merge_dictionary(d1, d2):
    merged = {}
    merged.update(d2)
    merged.update(d1)
    return merged

def q12():
    print('\nquestion 2')
    dict1 = {'Ten': 10, 'Twenty': 20, 'Thirty': 30}
    dict2 = {'Thirty': 40, 'Forty': 40, 'Fifty': 50}
    print(merge_dictionary(dict1, dict2))

def get_num_length(num):
    counter = 0
    temp = num
    while temp>0:
        counter += 1
        temp //= 10
    return counter

def num_count1(l1):
    d = {}
    for num in l1:
        length = get_num_length(num)
        d[length] = d.get(length,0)+1 
    return d


def q13():
    l1 = [35, 45, 5, 623, 3482, 2323432, 223, 4122, 23451, 34]
    d = num_count1(l1)
    print(d)


def num_count2(l1):
    d = {}
    for num in l1:
        length = get_num_length(num)
        d[length] = d.get(length,[]) + [num]
    return d

def q14():
    l1 = [35, 45, 5, 623, 3482, 2323432, 223, 4122, 23451, 34]
    d = num_count2(l1)
    print(d)


def anagram(l2):
    pass


def q15():
    l1 = ['hi', 'hello', 'bye', 'helol', 'abc', 'cab',
          'bac', 'silenced', 'licensed', 'declines']
    print(anagram(l1))


def print_dict(d1):
    if not d1:
        return
    print('{')
    for item in d1.items():
        print(f'\t\'{item[0]}\': {item[1]},')
    print('}')

def create_dict1(d1, d2):
    pass


def create_dict2(d1, d2):
    pass


def q16():
    countries_info = {
        "California": {
            "Capital": "Sacramento",
            "Big Cities": ["Los Angeles", "San Diego", "San Jose", "Sacramento"]
        },
        "Texas": {
            "Capital": "Austin",
            "Big Cities": ["Houston", "San Antonio", "Dallas", "Austin"]
        },
        "New York": {
            "Capital": "Albany",
            "Big Cities": ["New York City", "Buffalo", "Albany"]
        },
        "Florida": {
            "Capital": "Tallahassee",
            "Big Cities": ["Miami", "Tampa", "Orlando", "Tallahassee"]
        },
        "Illinois": {
            "Capital": "Springfield",
            "Big Cities": ["Chicago", "Springfield"]
        },
        "Pennsylvania": {
            "Capital": "Harrisburg",
            "Big Cities": ["Philadelphia", "Pittsburgh", "Harrisburg"]
        },
        "Ohio": {
            "Capital": "Columbus",
            "Big Cities": ["Columbus", "Cleveland", "Cincinnati"]
        },
        "Georgia": {
            "Capital": "Atlanta",
            "Big Cities": ["Atlanta"]
        },
        "Michigan": {
            "Capital": "Lansing",
            "Big Cities": ["Detroit", "Lansing"]
        },
        "North Carolina": {
            "Capital": "Raleigh",
            "Big Cities": ["Charlotte", "Raleigh"]
        }
    }
    cities_population = {
        "Los Angeles": 3970000,
        "San Diego": 1420000,
        "San Jose": 1030000,
        "Sacramento": 508529,
        "Houston": 2310000,
        "San Antonio": 1580000,
        "Dallas": 1340000,
        "Austin": 978908,
        "New York City": 8400000,
        "Buffalo": 255000,
        "Albany": 97400,
        "Miami": 2920000,
        "Tampa": 399700,
        "Orlando": 287442,
        "Tallahassee": 194500,
        "Chicago": 2700000,
        "Springfield": 116250,
        "Philadelphia": 1580000,
        "Pittsburgh": 302407,
        "Harrisburg": 49528,
        "Columbus": 892533,
        "Cleveland": 381009,
        "Cincinnati": 309317,
        "Atlanta": 498044,
        "Detroit": 670031,
        "Lansing": 118427,
        "Charlotte": 885708,
        "Raleigh": 474069
    }
    d1 = create_dict1(countries_info, cities_population)
    print_dict(d1)
    print("\nQuestion 3a:")
    d1 = create_dict2(countries_info, cities_population)
    print_dict(d1)


def q17():
    sample_set = {"Yellow", "Orange", "Black"}
    sample_list = ["Blue", "Green", "Red"]


def q18():
    set1 = {10, 20, 30, 40, 50}
    set2 = {30, 40, 50, 60, 70}


def q19():
    set1 = {10, 20, 30, 40, 50}
    set2 = {30, 40, 50, 60, 70}


def q20():
    set1 = {10, 20, 30}
    set2 = {20, 40, 50}


def main():
    # q1()
    # q2()
    # q3()
    # q4()
    # q5()
    # q6()
    # q7()
    # q8a()
    # q8b()
    # q9()
    # q10()
    # q11()
    # q12()
    # q13()
    q14()
    # q15()
    # q16()
    # q17()
    # q18()
    # q19()
    # q20()


if __name__ == '__main__':
    main()
