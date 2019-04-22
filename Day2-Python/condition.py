# create an empty distionary call 'days_i_poop'

days_i_poop = {}

# Ask user for for what day do they poop and how many times 
# (hint: you may need ask the user separately)

days = input(" what day do you poop? ")
poop = input(" how many times you pooped that day? ")

# Populate the 'days_i_poop' dictionary with each day of the week as KEY

days_i_poop[days] = int(poop)

# Populate the amount of time the user poop as integer as VALUE

# print out entire 'days_i_poop' dictionay

# Loop through the keys and value of 'days_i_poop' dictionay and print them individually