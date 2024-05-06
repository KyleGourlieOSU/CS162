"""
assign_5.py - This program practices linear and binary searches for integers within a 100-element list

Kyle Gourlie

Date Completed: 5/5/2024

This program practices the technique of linear and binary searching algorithms for a given 100-element array. First, the array
is generated, given lower and upper bounds. Each element in the array is randomly generated, and then sorted by numerical order.
The linear algorithm looks at each element in the list, and checks to see if it is equal to the inputted integer. Once the inputted
integer is larger than the element in the array, then the algorithm quits. The binary algorithm looks at the middle element in the
array, and checks to see if it is the element that is being searched for. If it is not the element, then either the lower half or upper
half of the array is removed from being searched based on whether or not the element located in the middle is greater than or less than
the desired array. This half-ing of the array continues until the array is no longer or the element is found. At the end, a conditional
statement is checked to see if both methods agree with each other. The binary and linear search algorithms will both return the element's
index where it is located. If it can't be found, it will return None.
"""

#imports
import random, time

#important constants
spd = 0.125

def int_list():
    """
    Creates a list of integers, and asks for user input to select an integer from the range contained in the list
    """
    #specification of the list of integers
    low = 0
    high = 1000
    num_int = 100
    ints = []
    #creates list
    for i in range(num_int):
        ints.append(random.randint(low,high))
    ints.sort()
    print(f'\nList of Integers:\n{ints}')
    #User input for integer selection
    while True:
        print()
        try:
            wnt_num = int(input(f'Enter a INTEGER you wish to find between {min(ints)} and {max(ints)}: '))
            if min(ints) <= wnt_num <= max(ints):
                break
            else:
                print(f'Value {wnt_num} is not within the range. Try again.')

        except ValueError:
            print(f'The value you have entered is NOT an integer. Please try again.')
    return ints, wnt_num


def lin_srch(int_ls: list, int_srch: int):
    """
    Linear search algorithm for looking for inputed integer.

    returns i (int): The index where the inputed integer exists
    returns None: If the inputed integer is not in list, then returns None
    """
    #iteration loop
    for i in range(len(int_ls)):
        print(f"\ninteger: {int_ls[i]}")
        print(f"wanted integer: {int_srch}")
        time.sleep(spd)
        if int_ls[i] == int_srch:
            print(f"Found entered value {int_srch} at index {i}\n")
            return i
        elif  int_ls[i] > int_srch:
            return None
        else:
            print("Have not found entered value\n")
    return None

def bin_srch(int_ls: list, int_srch: int):
    """
    Binary search algorithm for looking for inputed integer

    returns half (int): The where the inputed integer exists
    returns None: If the inputed integer is not in list, then returns None
    """
    found = False
    lower = 0
    higher = len(int_ls)-1
    while lower <= higher:
        time.sleep(spd)
        half = (lower+higher) // 2
        if int_ls[half] == int_srch:
             print(f"Found entered value {int_srch} at index {half}\n")
             return half
        
        elif int_ls[half] < int_srch:
            lower = half + 1
            new_ls = int_ls[half:]
            print(new_ls)
            print()

        elif int_ls[half] > int_srch:
            higher = half -1
            new_ls = int_ls[:half]
            print(new_ls)
            print()

    if found == False:
        print(f"Entered number {int_srch} is not contained in list")
        return None

def main():
    """main function"""
    int_ls, wnt_num = int_list()
    lin_index = lin_srch(int_ls,wnt_num)
    bi_index = bin_srch(int_ls, wnt_num)

    if lin_index == bi_index:
        print('\nLinear Search and Binary Search Agree')
    else:
        print('\nLinear Search and Binary Search Don\'t Agree')









