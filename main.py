# # # # def convert_to_celc(temp_farenheits: float) -> float:
# # # #     return round((temp_farenheits - 32)* 5 / 9, 2)
# # # # print(f"Room temperature: {convert_to_celc()} Farenheits")

# # # def print_letter(letter:str, *params, **keywordargs) -> None:
# # #     print(letter)
# # #     if params:
# # #         print(f"Args: {params}")
# # #     if keywordargs:
# # #         print(f"Kwargs: {keywordargs}")
# # # print_letter("a", "25", 22, name="Antanas")

# # # def add_two_nums(a:float, b:float = 10) -> float:
# # #     return a + b
# # # print(f"Sum of numbers: {add_two_nums(5,465)}")

# # # Lambda functions:
# # # def multiply(x:int, y:int) -> int:
# # #     return x*y
# # # print(multiply(2,3))

# # # multiplication = lambda x,y: x*y
# # # print(multiplication(2,3))

# # # add_default_quantity = lambda quantity: quantity + 25 
# # # print(add_default_quantity(5))

# # # 1) Create a function which converts lenght, mass, time units from SI system to CGS. 
# # # All arguments must hold default values if not provided. - centimeters, grams, seconds. 

# # def convert_to_cgs(length_si:float = 2.5, mass_si:float = 1.7, time_si:float = 15.2) -> None:
# #         print(f"""\nLength in CGS is: {length_si*100} centimeters; 
# #         \nMass in CGS is: {mass_si*1000} grams;
# #         \nTime in CGS is the same as time in SI units: {time_si} seconds.""")
# # convert_to_cgs(time_si = 15)

# # # 2) Create a program which takes 5 random number per 1 input.
# # # The create a function which takes the sum of those numbers (lets agree argument is being called 'num_sum'),
# # # and all those 5 numbers as separate free arguments as well.
# # # Multiply all those numbers with with the num_sum you calculated in a list data structure.

# # from typing import List

# # def multiplying_with_the_sum(num_sum: float, *args: float) -> List[float]:
# #     list_of_multiplications = [num * num_sum for num in args]
# #     return list_of_multiplications
# # nums_from_user = input("\nPlease provide me with 5 random digits separated by commas: ")
# # num_list = [float(num) for num in nums_from_user.split(',')]
# # sum_of_numbers = sum(num_list)

# # print(f"\nThis is a list that gets made after we multiply every your given number with the sum of all the numbers you have provided: {multiplying_with_the_sum(sum_of_numbers, *num_list)}")


# # # 3) Create lamba functions for these caclulations:
# # #  - calculate circle radius
# # #  - calculate average speed of the car (knowing distance and time passed to drive that distance)
# # #  - calculate percentage of value if 5500 is equal 200%

# # circle_radius_from_circumference = lambda circumference: round(circumference / (2 * 3.14), 2)
# # print(f"\nRadius of the circle with the circumference you have provided is: {circle_radius_from_circumference(15)}")

# # average_speed_of_the_car = lambda distance, time: round(distance / time, 2)
# # print(f"\nAverage speed of the car is: {average_speed_of_the_car(500, 2)} distance units per time units")

# # calculating_percentage_of_value = lambda value_to_check: round(value_to_check * 200 / 5500, 2)
# # print(f"\nYour inserted value is just {calculating_percentage_of_value(17)} % ")



# # Write a function that takes two lists and adds the first element in the first list with the first element 
# # in the second list, the second element in the first list with the second element in the second list,
# #  etc, etc. Return True if all element combinations add up to the same number. Otherwise, return
# # False. Example:

# from typing import Union, List

# def check_sums_of_lists(list_first: List[Union[float, int]], list_second: List[Union[float, int]]) -> bool:
#     list_of_sums = [elem_1 + list_second[index] for index, elem_1 in enumerate(list_first)]
#     return list_of_sums.count(list_of_sums[0]) == len(list_of_sums)

# first_list = [4, 4.0, 4, 4, 4]
# second_list = [4, 4.0, 4, 4, 4]

# print(check_sums_of_lists(first_list, second_list))


# There's a great war between the even and odd numbers. Many numbers already lost their lives in this war and it's 
# your task to end this. You have to determine which group sums larger: the evens or the odds. The larger group wins.

# Create a function that takes a list of integers, sums the even and odd numbers separately, then returns the difference 
# between the sums of the even and odd numbers.

from typing import List

list_of_nums = [64,12,48,1,34,33,37,15,16,17,19,23,27,29]

def war_of_nums(list_of_numbers: List[int]) -> int:
    sum_of_evens = sum([num for num in list_of_numbers if num%2==0])
    sum_of_odds = sum([num for num in list_of_numbers if num%2==1])
    return sum_of_evens - sum_of_odds
print(war_of_nums(list_of_nums))