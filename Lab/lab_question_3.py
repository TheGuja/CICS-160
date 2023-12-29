def hello_world():
    print("Hello World")

def age_compare():
    person_1 = input("Enter a person's name: ")
    age_1 = int(input("Enter their age: "))

    person_2 = (input("Enter a person's name: "))
    age_2 = int(input("Enter their age: "))

    if (age_1 > age_2):
        print(f"{person_1} is {age_1 - age_2} years older than {person_2}")
    elif (age_2 > age_1):
        print(f"{person_2} is {age_2 - age_1} years older than {person_1}")
    else:
        print(f"{person_1} and {person_2} are the same age")

def while_loops():
    sum = 0
    input_num = float(input("Enter a number: "))

    while (input_num) > -1:
        sum += input_num
        input_num = float(input("Enter a number: "))

    print(sum)

def for_loops_and_list():
    num_numbers = int(input("How many numbers would you like to enter? "))
    nums = []

    for i in range(num_numbers):
        nums.append(float(input("Enter your number: ")))

    nums = nums[::-1]
    for num in nums:
        print(num)