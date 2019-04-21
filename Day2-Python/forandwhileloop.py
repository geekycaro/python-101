# The list of candies to print to the screen
candyList = ["Snickers", "Kit Kat", "Sour Patch Kids", "Juicy Fruit", "Swedish Fish",
             "kind bar", "Hershey Bar", "Skittles", "Starbursts", "M&Ms"]

# The amount of candy the user will be allowed to choose
#allowance = 5
greedy = "yes"
# The list used to store all of the candies selected inside of
candyCart = []

# Print the list of candies provided to you in the file along with their index numbers stored in brackets beside them.
for candy in candyList:

    print("[" + str(candyList.index(candy)+1) + "]" + candy)
    

# Run through a loop which will prompt the user to choose which candies to take home with them
while greedy == "yes":
    allowance_candy = input("Which candy would you like to bring home? ")

    # Add the candy at the index chosen to the candyCart list
    candyCart.append(candyList[int(allowance_candy)-1])
    #print(candyList[int(allowance_candy)-1])
    greedy = input("You fatass want more candy? ")
# Loop through the candyCart to print what candies were brought home
print(candyCart)
for candychoice in candyCart:
    print(candychoice)