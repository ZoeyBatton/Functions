# parameters are when you pass through a value in a function. That value goes inside of the ()

char_name = input("What is your name?: ")
char_role = input("What character role are you?: ")

def my_function(the_name, the_role):
    print(f"Your name is {the_name}.")
    print(f"Your character role is {the_role}.")
my_function(char_name, char_role)

char_name2 = input("What is your name?: ")
char_role2 = input("What character role are you?: ")

my_function(char_name2, char_role2)