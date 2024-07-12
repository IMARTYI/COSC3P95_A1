
import random
import string


# Function made to generate a random string with upper case letters, lower case letters and numbers.
def random_generator():
    rand_str = ""

    str_len = random.randint(0,10)

    for char in range(str_len):

     rand_numb= random.randint(1,3) # Random number generator


     if rand_numb == 1:
        char = random.choice(string.ascii_letters)
        rand_str+= char.lower()

     if rand_numb ==2: # Generate a
        char = random.choice(string.ascii_letters)
        rand_str += char.upper()

     if rand_numb == 3: # Generate a numerical value
        char = str(random.randint(0,9))
        rand_str += char

    return rand_str


# Function to check to see if there are duplicate numbers within the strings.
def test_function(input_str):

    for i in range(len(input_str)-1):
        if input_str[i].isnumeric():
            if input_str[i] == input_str[i+1]:
                return True


    return False


# The Following Function was an attempt to implement delta de-bugging for 5 b in a binary search
def delta_debugging(test_str):

    list_size = len(test_str)
    start_index = 0
    end_index = list_size - 1

    while start_index <= end_index:

        mid = (start_index + end_index) // 2

        sub_string = test_str[start_index: mid]

        i = test_function(sub_string)

        if i ==True:
            end_index = mid-1

        else:
            start_index= mid +1




    return test_str[start_index: end_index-1]


# Initial Function given

def processString(input_str):
    output_str = ""
    for char in input_str:
        if char.isupper():
            output_str += char.lower()
        elif char.isnumeric():
            output_str += char * 2
        else:
            output_str += char.upper()

    return output_str


# Testing cases via random testing with 5 random cases
def random_test_case():

    for i in range(5):
        str = random_generator()

        print("INPUT: " + str)

        print("OUTPUT: " + processString(str))

# Array containing all the test cases
test_strings=[
    "abcdefG1 ",
    "CCDDEExy",
    "1234567b",
    "8665"
]


print("PART A:")


random_test_case()

print()

print("PART B: ")
print("INPUT STRING: " + test_strings[0])

print("OUTPUT STRING: " + processString(test_strings[0]))

output_string = processString(test_strings[0])
print("TRIMMED: " + delta_debugging(output_string))




