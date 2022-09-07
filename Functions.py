# DRY- Don't Repeat Yourself.


def directions():
    print("Turn left out of parking lot")
    print("Drive to stop light and turn left")
    print("Drive one mile through Canfield.")
    print("Starbucks is across the street from Sheetz")
    print("Turn left into Starbucks")

# directions()

number_of_people = int(input("How many people are asking for directions?: "))

while number_of_people > 0:
    print(f"{number_of_people}- New Directions")
    directions()
    number_of_people = number_of_people - 1