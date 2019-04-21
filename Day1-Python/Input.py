# Create a variable called user_name that captures the user's first name.
user_name = input("What's your name ")

# Create a variable called neighbor_name that captures the name of the user's neighbor.
neighbor_name = input("What's his name? ")

# Create variables to capture the number of months the user has been coding.
how_long = input("how long have you been coding? ")

# Create variables to capture the number of months the user's neighbor has been coding.
how_long1 = input("how long has he been coding? ")

# Use math to calculate the combined months coded between the two users. 
combined = int(how_long) + int(how_long1)

# Store this in a variable called total_months_coded.


# Print results in the form:
# I am <user_name> and my neighbor is <neighbor_name>
# Together we have been coding for <total_months_coded> months!

print ("I am " + user_name + " and my neighbor's name is " + neighbor_name)
print ("Together we have been coding for " + str(combined))
