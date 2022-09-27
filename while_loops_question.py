num_1 = 3.4
num_2 = 7

def my_function():
    quiz = float(input(f"What is the {num_1} + {num_2}?: "))
    while(quiz != (num_1 + num_2)):
        print("No. Thats wrong, try again")
        my_function()
    print("Congrats. Thats the correct answer.")

my_function()