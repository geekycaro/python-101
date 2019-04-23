# create an empty distionary call 'days_i_poop'
days_i_poop = {}
# Populate the 'days_i_poop' dictionary with each day of the week as KEY
pooped = "yes"

while pooped == "yes":
    when_i_poop = input("What day do you poop? ") 
    times_i_poop = input("How many times? ")
    days_i_poop[when_i_poop] = int(times_i_poop)
    pooped = input("Did you poop everyday? ") 

days_i_poop[days] = int(poop)

# Populate the amount of time the user poop as integer as VALUE

# print out entire 'days_i_poop' dictionay
print(days_i_poop)
# Loop through the keys and value of 'days_i_poop' dictionay and print them individually
for pooped, times in days_i_poop.items():
    print(pooped,times)
