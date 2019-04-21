# Dictionary full of info
bio = {
    "name": "Carolina",
    "age": 27,
    "hobbies": [
        "hiking",
        "tennis",
        "ice skating"
    ],
    "waking": {
        "monday": 9,
        "tuesday": 9,
        "wednesday": 9,
        "thursday": 9,
        "friday": 9,
        "saturday": 10,
        "sunday": 10}
}
# Print out results are stored in the dictionary

print("Hello I am " + bio["name"] + " and my hobby is " + bio["hobbies"][0])
print("I have " + str(len(bio["hobbies"])) + " hobbies!")
print("On the weekend I get up at" + str(bio["waking"]["saturday"]))