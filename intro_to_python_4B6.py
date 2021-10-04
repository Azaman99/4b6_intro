new_black = 10
# print(new_black)
# print(type(new_black))

# float_me = 0.5
# print(float_me)
# print(type(float_me))

 
stringify = "We had a downpour in Lagos 2 days ago!"
# print(stringify)
# print(type(stringify))

my_verdict = True
# print(my_verdict)
# print(type(my_verdict))

random_stuff = ['music', "sports", True, 99.9]
# print(random_stuff)
# print(type(random_stuff))

new_guy = ("45", False, 101)
# print(new_guy)
# print(type(new_guy))

sports = {"football", "cricket", "basketball", "cricket"}
# print(sports)
# print(type(sports))


my_info = {
    "name" : "Adamu",
    "gender" : "Male",
    "age" : 12
}

# print(my_info)
# print(type(my_info))




###ARITHMETIC OPERATIONS
my_mod = 33 % 4
# print(my_mod)


my_quote = 33 // 4
# print(my_quote)

r_power = 5 ** 4
# print(r_power)


####COMAPRISON OPERATORS
first_num = 67
second_num = 40

# quick_check = first_num != second_num
# print(quick_check)

# feedback = ((first_num % 2 != 0) or (second_num > first_num)) and not((second_num == 40) or (second_num // 2 != 0))
# print(feedback)

career = "She is a model who lives in California"
# output = "She I" in career

# scores = [62, 55, 72, 89]
# check = 62 in scores

# print(check)


###CONTATENATION
# first_phrase = "Hello"
# second_phrase = "there, welcome!"

# full_sent = first_phrase + " " + second_phrase
# print(full_sent)


career = "She is a model who lives in California!"
desired_char = career[-1]
desired_portion = career[ : 10]
# print(desired_portion)


# age_limit = 10
# report_template = "You can't gain access unitl your are {} years old.".format(age_limit)

# report_template = f"You can't gain access unitl your are {age_limit} years old."

# print(report_template)


##ESCAPE CHARACTER
source_of_income = 'The nation\'s crude oil'
# print(source_of_income)

refined_career = career.title()

quick_search = career.startswith("She is")

# another_search = career.index("nigeria")
# print(another_search)

# print(refined_career)

career = "!She is a model who lives in California!"
trans_list = career.split("!")
# print(trans_list)

new_career = career.replace("California", "Texas")
# print(new_career)

trimmed = career.lstrip("!")
# print(trimmed)


####LIST
random_stuff = ["pawn", "phone", "pen", "ball", False, 99.69, "pawn", 2021, 4+2j, "water"]
# print(random_stuff)

desired_item = random_stuff[-1]
# print(desired_item)

desired_items = random_stuff[ : : 3]
# print(desired_items)

random_stuff[1] = "water"

random_stuff[3 : 6 : 2] = ["chair", True]


# print(random_stuff)

no_of_occurence = random_stuff.count("water")
# print(no_of_occurence)

# print(random_stuff.index("pawn"))

random_stuff.remove("water")

random_stuff.append("Checkmate")

# print(random_stuff)

backup_list = random_stuff.copy()
# print(backup_list)

random_stuff.insert(0, "awesome")
# print(random_stuff)

scores = [31, 19, 20, 56, 45]
# print(scores)
# print("\n")
scores.sort(reverse = True)
# print(scores)


# print(random_stuff)
# print("\n")
# random_stuff.reverse()
# print(random_stuff)

quick_one = ("Brilliant", "Shy", "Great")
# print(quick_one[1:])

# quick_one[1] = "Bold"
# print(quick_one)





####SETS
grocery_cart1 = {"Bread", "Oranges", "Jam", "Fruit Juice", "Eggs", "Butter", "Cookies"}
grocery_cart2 = {"Eggs", "Yam", "Grapes", "Cookies", "Apple", "Carrot", "Bread", "Ice Cream"}

# print(grocery_cart1)
# print(grocery_cart2)

grocery_cart2.discard("Yam")
grocery_cart2.add("Youghurt")
# print(grocery_cart2)

merged_carts = grocery_cart1.union(grocery_cart2)
# print(merged_carts)

# grocery_cart1.update(grocery_cart2)
# print(grocery_cart1)

backup_cart1 = grocery_cart1.copy()
backup_cart2 = grocery_cart2.copy()

cart1_only = grocery_cart1.difference(grocery_cart2)
# print(cart1_only)

# grocery_cart2.difference_update(grocery_cart1)
# print(grocery_cart2)

common_groceries = grocery_cart1.intersection(grocery_cart2)
# print(common_groceries)

backup_cart1.intersection_update(backup_cart2)
# print(backup_cart1)

taking_out_duplicates = grocery_cart1.symmetric_difference(grocery_cart2)
# print(taking_out_duplicates)
 

#####DICTIONARIES!!!
# customer_info = {
#     "name" : ["Mike Aubentraut", "Uzo Chuks", "Tom Whiteside", "Mary Jane"],
#     "gender" : ["Male", "Male", "Male", "Female"],
#     "age" : [22, 29, 34, 18],
#     "nationality" : ["American", "Nigerian", "Canadian", "Jamaican"]
# }

# print(customer_info)

# all_names = customer_info["name"]
# # print(all_names)

# all_nationalities = customer_info.get("nationality")
# # print(all_nationalities)

# all_keys = customer_info.keys()
# # print(all_keys)

# all_values = customer_info.values()
# # print(all_values)

# all_items = customer_info.items()
# # print(all_items)

# customer_info.update({"occupation" : ["Actor", "Banker", "Footballer", "Experience Engineer"]})

# customer_info.pop("age")

# customer_info.clear()
# print(customer_info)



####BUILTIN FUNCTIONS
# get_data = input("Enter integers here: ")
# #to have access to the integers
# con_list = get_data.split(" ")
# #to convert/change the entries to proper integers
# con_list[0] = int(con_list[0])
# con_list[1] = int(con_list[1])
# con_list[2] = int(con_list[2])
# con_list[3] = int(con_list[3])
# con_list[4] = int(con_list[4])

# # to find the smallest number from the given integer
# smallest_integer = min(con_list)
# print(smallest_integer)

# # to find the second largest number from the given integers
# new_list = list(set(con_list))
# new_list.sort()

# output = new_list[-2]

# print(output)

#Zip 
first_list = ["high", "low", "middle", "high-lows", "dark space"]
second_list = [1, 2, 3]

zipped_object = zip(first_list, second_list)
# print(list(zipped_object))

# Enumerate
first_list = ["high", "low", "middle", "high-lows", "dark space"]
volts = enumerate(first_list)
# print(list(volts))

# Lambda
crush = lambda x : x.upper()
output = crush("tony")
# print(output)

# Map
# This executes a specified function for each item in an iterable. Its syntax is; map(function, iterable).
# Similarly, to view the mapped object, convert it to a list.
scores = [68, 72, 83, 92]
upgraded = map(lambda x : x + 2, scores)
results = list(upgraded)
# print(results)

# for string
words = ["new", "old", "used"]
upgraded_word = map(lambda x : x.title(), words)
results_word = list(upgraded_word)
# print(results_word)

# Filter
# This filters an iterable in accordance with a specified function. It returns a list of the items that returned True in that function.
# Similarly, it returns a filter object which can be viewed by converting to a list.

# this is to filter a list of odd numbers
sam = [20, 31, 45, 60, 10, 77]
filt = filter(lambda x : x % 2, sam)
done = list(filt)
# print(done)


# using a membership operator to filter the string with "e" in it.
names = ["Sub-Zero", "Scorpion", "Raiden", "Fujin", "Quan Chi", "Tanya"]
filt = filter(lambda x : "e" in x, names)
new_names = list(filt)
# print(new_names)

# Range
# This function returns a sequence of numbers.Its general sequence is range(start, stop, step).
even = range(0, 20)
even_num = list(even)
# print(even_num)

# Built in modules
# Time
from hashlib import new
import time
# print("What is your name")
# time.sleep(7)
# print("My name is Anthony")

# Random
import random as rd
rd.seed(99)
names = ["Sub-Zero", "Scorpion", "Raiden", "Fujin", "Quan Chi", "Tanya"]
rd.shuffle(names)
# print(names)

# for random choice you should assign it to a variable.
names = ["Sub-Zero", "Scorpion", "Raiden", "Fujin", "Quan Chi", "Tanya"]
ran_pick = rd.choice(names)
# print(ran_pick)

# for random sample you should assign it to a variable.
names = ["Sub-Zero", "Scorpion", "Raiden", "Fujin", "Quan Chi", "Tanya"]
ran_samp = rd.sample(names, 3)
# print(ran_samp)

ran_rdg = rd.randrange(14, 44, 2)
# print(ran_rdg)

# Datetime
from datetime import datetime as dt

curr_date_and_time = dt.now()
# print(curr_date_and_time)

curr_date_and_time = dt.now().hour
# print(curr_date_and_time)

curr_date_and_time = dt.now()
output = curr_date_and_time.strftime("%m")
# print(output)

ch_day = "25/12/2021"
conv_date = dt.strptime(ch_day, "%d/%m/%Y")
# print(conv_date.date())

notable_days = ["15/1/2021", "14/2/2021", "1/4/2021", "29/5/2021", "12/6/2021", "1/10/2021", "25/12/2021"]
new_day = map(lambda x : (dt.strptime(x, "%d/%m/%Y")).date(), notable_days)
new_not = list(new_day) 
# print(new_not)


# Conditionals
# if/else statement
# names = ["Sub-Zero", "Scorpion", "Raiden", "Fujin", "Quan Chi", "Tanya"]
# filt = filter(lambda x : len(x) >= 7, names)
# new_filt = list(filt)
# # new_names = len(names)
# # print(new_names)
# if  filt :
#     print("Yes")
# else :
#     print("No")

# if 5 > 8 or dt.now().minute % 2 == 0 :
#     print("Definitely")
# else :
#     pass

# if/elif/else statement
# if "e" in "Emmanuel" :
    # print("Spelt correctly")
# elif 59 > 58.9 :
    # print("Mathematically correct")
# else :
#     pass

# this is a program to take in string from the user and return if there is a duplicate letter in it.
# user = input("Enter a string : ")
# new_user = set(user)
# print(set(user))
# if len(new_user) != len(user) :
#     print("It contains duplicates")
# else : 
#     print("It does not contain duplicate")

# LOOPS 
# WHILE LOOP
# cracker = 1 
# while (cracker < 5):
#     if cracker == 3:
#         print("I'm outta here")
#         break
#     else:
#         print("Cracker is less than 5")
#         cracker = cracker + 1

# Ending and Unending while loop
# A program that takes in two integer, the first being smaller than the other. the program will select intger btwn that range of the selected number and the user would guess which number the program selects.
### Guess Game###
# import random as rd
# get_data = input("Enter two integers here: ")
# con_list = get_data.split(" ")
# # converting to integers
# con_list[0] = int(con_list[0])
# con_list[1] = int(con_list[1])

# # randomly selecting an integer within the given range
# random_integer = rd.randrange(con_list[0], con_list[1])

# # time to guess the number
# while True:
    # guess = input("Enter your guess here: ")
    # if random_integer == int(guess):
    #     print("You are correct!")
    #     break
    # elif int(guess) < random_integer:
    #     print("Guessed too Low... try again")
    # elif int(guess) > random_integer:
    #     print("Guessed too high... try again")
    # else:
    #      pass

###FOR LOOP
# iterables u can use in for loop are string, list, set, tuple, dict, zip, enumerate, range.
# new_word = "Multiverse"
# for i in new_word:
#     print("Home of Marvel")

# Enummerate
# new_list = ["pop", "rock", "country"]
# for index, item in enumerate(new_list):
#     print(index, item)

# scores = [64, 72, 67, 98, 21, 23]
#     for num in scores:
#         if num % 2 == 0:
#             print(f"{num} is an even number")
#         elif num % 2 != 0:
#             print(f"{num} is an odd number")
#     else: 
#         pass

# DICT
customer_info = {
    "name" : ["Mike Aubentraut", "Uzo Chuks", "Tom Whiteside", "Mary Jane"],
    "gender" : ["Male", "Male", "Male", "Female"],
    "age" : [22, 29, 34, 18],
    "nationality" : ["American", "Nigerian", "Canadian", "Jamaican"]
}

for entry in customer_info.items():
    print(entry[0][1])
    print("\n")

# ZIP
# continents = ["Africa", "Asia", "Europe", "South America", "North America", "Antartica", "Australia"]
# countries = ["Nigeria", "Japan", "England", "Brazil", "Canada", "Antartica", "Australia"]

# zipped_object = zip(countries, continents)

# for entry in zipped_object:
#     print(entry)

# Write a program to accept integer input from the user and return a list of 10% increase in the value supplied.
# get_num = input("Enter integer values here: ")
# con_list = get_num.split(" ")

# using loop
# converting to integers
# for i in range(len(con_list)):
#     con_list[i] = int(con_list[i])

# for x in range(len(con_list)):
#     con_list[x] *= 1.1
    # con_list[x] = round(con_list[x], 2)
# print(con_list)

# OR
# percent = []
# for a in con_list:
#     a = a * 1.1
#     percent.append(a)
# print(percent)

# using map
# converting to integer
# new_list = map(lambda x : int(x), con_list)

# # to increment
# output = list(map(lambda x : round(x * 1.1, 2), new_list))
# print(output)


####2 - LEVEL NESTED LOOP
# For Each iteration in the outer loop, the inner loop gets executed and completed.
# nouns = ["Cars", "Countries", "Lady"]
# adjectives = ["Fast", "Beautiful", "Awesome"]

# for qualifier in adjectives:
#     for word in nouns:
#         print(qualifier, word)

####3 - LEVEL NESTED LOOP
# For Each iteration in the outermost loop, the middle loop gets executed and completed and while the middle loop gets completed, the innermost loop gets executed and completed.
# starters = ["The", "A", "An"]
# nouns = ["Cars", "Countries", "Lady"]
# adjectives = ["Fast", "Beautiful", "Awesome"]

# for beginner in starters:
#     for qualifier in adjectives:
#         for word in nouns:
#             print(beginner, qualifier, word)

#     print("\n")

###LIST COMPREHENSION####

scores = [60, 62, 64, 66, 72, 81, 93, 47, 58]

upgraded = [i + 3 for i in scores]
# print(upgraded)

new_ugrade = [ i + 3 for i in scores if i % 2 == 0]
# print(new_ugrade)

###Sorted method###This is used to sort iterables that are mixed
new_list = [("Awesome", 12), ("Zebra", 2), ("Dawn", 9), ("New", 4)]
sorted_list = sorted(new_list, key= lambda a : a[1])
# print(sorted_list)