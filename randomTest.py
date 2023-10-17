# David Martin
# 6995948

import math
import random

print("Bubble Sort Testing")

# Implementing Bubble Sort
# Arr: array input
# n: length of the array
def bubble_sort(arr, n):

    for i in range(n):
        for j in range(0,n-i-1):
            if arr[j] > arr[j+1]:
                arr[j],arr[j+1] = arr[j+1],arr[j]

    return arr

# Function to print the output of the array
def print_array(arr):

    for i in range(len(arr)):
        print(arr[i], end=' ')


# Function to check if the test case passed or not
def check_sorted(arr):

    if arr == sorted(arr):
        print("The Test Case Was Passed")
    else:
        print("The Test Case Failed")


# Function that is implementing random test case generator
# With random length array from 0-10 and each value is randomly generated from 0-1000

def random_test_case():

    for x in range(10):  # Loop to run 10 different test cases

        rand_len = random.randint(0,10) # Generate the length of the randomly genreated array

        rand_arr = []

        for i in range(rand_len): # Loop to generate the random values within the array
            rand_numb = random.randint(0,1000)

            rand_arr.append(rand_numb) # add random integers into the array


        print("Input Array : ") # Display the input array before calling bubble sort

        print_array(rand_arr)

        bubble_sort(rand_arr,len(rand_arr)) # Call bubble sort for the random array
        print()

        print("Output Array: ") # Print the contents of the sorted array

        print_array(rand_arr)

        print()

        check_sorted(rand_arr) # Call check_sorted to ensure the array matches the expected output


random_test_case() # Calling the test case generator




