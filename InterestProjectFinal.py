# Starting text 
print("Hello, welcome to my project. This is my first portfolio project and I am so excited to share with you my knowledge on interest equations. I have just learned how to use git tracking so I am very excited. Let's start learning!")
print("There are three types of interest: Simple Interest, Compound Interest, Complex Compound Interest, and Continuous Interest.")
print("Type which interest you would like to learn about: ")
key = "A is amount after interst, P is initial amount, t is time in years, and r is percentage rate as in the interest"

# Equation functions
def simple_interest(initial_amount):
    
    amount = (5 * .1 + 1) * float(initial_amount)
    return amount


# Choices
def choices():
    interest_input = input()
    if interest_input == "Simple Interest":
        print(key)
        print("An example of simple interest is if you give 100 dollars away at 10% simple interest for every year, then you would get 10% of 100 every year so you would get 100 + 10 + 10 + 10...")
        print("The equation is: A = P(1+tr)")
        print("Now let's try this equation ourselves. Give me a starting amount for simple interset for 5 years and 10%")
        simple_interest_input = input()
        print(simple_interest(simple_interest_input))
        print("This is the amount of money you will have after 5 years with simple interest of .10 with a starting amount of " + simple_interest_input)
        print("You can continue learning about other interests by typing another type below or simply exit. Thank you! ")
        choices()

choices()