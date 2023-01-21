# Declare an empty list named `our_list`.
our_list = []

# Use the `append` list function to append the number 1 into `our_list`.
our_list.append(1)

# Append the string "hello" into `our_list`.
our_list.append("hello")

# Append the boolean False into `our_list`.
our_list.append(False)

# Append the number 84 into `our_list`.
our_list.append(84)

# Append the string "world" into `our_list`
our_list.append("world")

# Print `our_list`
print(our_list)

# Declare a variable named `one_to_ten` and assign it an list containing the numbers from 1 to 10.
one_to_ten = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Print the 4th element from `one_to_ten`.
print(one_to_ten[3])

# Print the 7th element from `one_to_ten`.
print(one_to_ten[6])

# We've declared this list for you
num_list = [2, 65, 3, 7, 39, 22, 11, 94, 299, 9, 20, 21, 51, 37]

# Iterate through the provided `num_list` and create an if-else statement to print every number greater than 50
index = 0
total_sum = 0
for numbers in num_list:
    if numbers > 50:
        print(numbers)
    
    if numbers == 11:
        print(f'num_list[{index}] is 11')
    index += 1
    total_sum = total_sum + numbers
print(total_sum)
    
# Iterate through the provided `num_list` and use the `index` function to print the index of the first occurrence of the number 11.
    

# Iterate through the provided `num_list` and print the sum of all the numbers.


# Iterate through the provided `num_list` and create an if-else statement to print the sum of all the numbers greater than 50.


# Iterate through the provided `num_list` and create an if-else statement to print the sum of all the even numbers.


fruits = [
  "Apple", "Orange", "Banana", "Pomelo", "Apple", "Kiwi", "Peach", "Banana", "Grape", "Tomato",
  "Kiwi", "Apple", "Watermelon", "Lemon", "Pomelo", "Apple", "Banana", "Peach", "Apricot", "Grape"]

# Iterate through the provided `fruits` list and print the number of times "Apple" appears in the list.


# Iterate through the provided `fruits` list and print the number of times "Peach" appears in the list.


# Iterate through the provided `fruits` list and print the number of fruits that start with "P" in the list.


## Challenge

# Create a new empty list named `unique_fruits`.


# Iterate through `fruits` and populate `unique_fruits` with only unique values from `fruits`. Hint: try looking up "not in" conditionals for if statements


# Print out the `unique_fruits` list.


# In this challenge we're going to be working with nested lists.
# You can store any type of data within an list- even other lists!
two_dim_list = [
  [54, 6, 7, 46, 78],
  [43, 9, 6, 65, 65],
  [32, 1, 44, 1, 23],
  [55, 12, 2, 34, 2],
  [2, 12, 44, 2, 12]]

# Iterate through the first list inside `two_dim_list` and print all the numbers less than 25.


# Iterate through the second list inside `two_dim_list` and print all the numbers less than 25.


# Iterate through the fifth list inside `two_dim_list` and print all the numbers less than 25.



# Iterate through `two_dim_list` and the lists inside of it and print all the odd numbers.


# Iterate through `two_dim_list` and the lists inside of it and print the sum of all the numbers that are a multiple of 3.

