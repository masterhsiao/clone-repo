# Create a list called 'farm' with the elements "pig", "cow", "chicken", "dog", "horse", "sheep".
farm = ["pig", "cow", "chicken", "dog", "horse", "sheep"]

# Write an if statement that prints the string "RWAR!" if the first element of farm is NOT "Godzilla".
if farm[0] != "Godzilla":
    print("Rwar!")
# Write an else if statement that prints the string "SCREECH!" if the last element of farm is "Mothra".
elif farm[5] == "Mothra":
        print("Screech")
# Else, print the string "This animal is neither Godzilla nor Mothra!".
else:
    print("This animal is neither Godzilla nor Mothra!")

# Declare a variable named 'dog' with a string of "Spot".
dog = "spot"
# Declare 3 variables `cat`, `city`, `car` without assigning them values.

cat = None
city = None
car = None

# Assign the string "Farley" to `cat`.
cat = "Farley"

# Assign the string "San Francisco" to `city`.
city = "San Francisco"

# Assign the string "Prius" to `car`.
car = "Prius"

# Using string concatenation, print out the sentence "See Spot run!".
print(f'See {cat} run!')

# Using string concatenation, print out the sentence "I drive Farley around San Francisco in my Prius".
print(f'I drive {cat} around {city} in my {car}')

# Declare a variable budget and assign it a value of 5000.
budget = 5000

# Declare a variable rent_cost and assign it a value of 1500.
rent_cost = 0

# Declare a variable utilities_cost and assign it a value of 150.
utilities_cost = 150

# Declare a variable food_cost and assign it a value of 250.
food_cost = 250

# Declare a variable transportation_cost and assign it a value of 350.
transportation_cost = 350

# Declare a variable computer_cost and assign it a value of 2000.
computer_cost = 10000

# Declare a variable called total_cost that takes the sum of all costs above (excluding budget).
total_cost = rent_cost + utilities_cost + utilities_cost + food_cost + transportation_cost + computer_cost

print(total_cost)

# Write an if statement that checks whether the sum of all our costs is within the budget.
if total_cost < budget:
# If so, print "You're total cost is " concatentated with the `total_cost` variable.
    print(f"You're total cost is {total_cost}")
# Else, print "You're over budget by " concatenated with the difference between `budget` and `total_cost`.
else:
    print(f"You're over budget by {budget - total_cost}")

# Write an if statement that checks whether the rent_cost is larger than the sum of the `utilities_cost`, `food_cost`,
if rent_cost > utilities_cost + food_cost + transportation_cost:
    print("The RENT is too dang high!")
# and `transportation_cost`. If so, print a string that says "The rent is too damn high!".
# Else, print a string that says "Ahhh just right!"
else:
    print("ahh just right!")
