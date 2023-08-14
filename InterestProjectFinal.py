# Starting text 
print("========================")
print("Hello, welcome to my project. This is my first portfolio project and I am so excited to share with you my knowledge on interest equations. I have just learned how to use git tracking so I am very excited. Let's start learning!")
print("There are three types of interest: Simple Interest, Compound Interest, Complex Compound Interest, and Continuous Interest.")
print("Type which interest you would like to learn about: ")
print("========================")

def key():
    print("This the Key: A is amount after interst, P is initial amount, t is time in years, n is the number of repititions, and r is percentage rate as in the interest")
    print("========================")



# Equation functions
def simple_interest(initial_amount):
    for i in range(1,10):
        amount = float(initial_amount) * (1 + i * .10)
        print(round(amount))
    return "End"

def compound_interest(initial_amount):
    for i in range(1, 10):
        exponent = 1.1 ** i
        print(round(exponent * float(initial_amount)))
    return "End"

def complex_compound_interest(compounds_per_year):
    print("This is the scenerio compounded monthly:")
    for i in range(1,11):
        exponent = 12 * i 
        divide = .05/12
        multiply = (1 + divide)
        mul2 = multiply ** exponent
        print(round(mul2 * 100, 4))
    
    print("This is the scenerio compounded " + compounds_per_year + " times:")
    for i in range(1,11):
        num = float(compounds_per_year)
        exponent2 = num * i 
        divide2 = .05/num
        multiply2 = (1 + divide2)
        mul22 = multiply2 ** exponent2
        print(round(mul22 * 100, 4))
    return "compounds_per_year"

def continuous_interest(continuous_interest_input):
    for i in range(1,11):
        num = i * .10
        num2 = 2.71828 ** num
        print(round(float(continuous_interest_input) * num2))
    return "End"


# Choices
def choices():
    interest_input = input()
    if interest_input == "Simple Interest":
        key()
        print("An example of simple interest is if you give 100 dollars away at 10% simple interest for every year, then you would get 10% of 100 every year so you would get 100 + 10 + 10 + 10...")
        print("The equation is: A = P(1+tr)")
        print("Now let's try this equation ourselves. Give me a starting amount for simple interset for 5 years and 10%")
        simple_interest_input = input()
        print(simple_interest(simple_interest_input))
        print("This is the amount of money you will have after 10 years with simple interest of .10 with a starting amount of " + simple_interest_input)
        print("You can continue learning about other interests by typing another type below or simply exit. Thank you! ")
        print("========================")
        choices()
    if interest_input == "Compound Interest":
        key()
        print("An example of compound interest is if you give 100 dollars away at 10% compounded interest for every year, the 10% gets compounded back into the initial amount for the first year which would yield a greater year for the second year than the first because you are getting 10 percent of 110 for the second year and looks like: 110, 121, 133.1...")
        print("The equation is: A = P(1+r)^t")
        print("Now let's try this equation ourselves. Give me a starting amount for compound interset for 10 years and 10%")
        compound_interest_input = input()
        print(compound_interest(compound_interest_input))
        print("The last number is the amount of money you will have after 10 years with simple interest of .10 with a starting amount of " + compound_interest_input)
        print("You can continue learning about other interests by typing another type below or simply exit. Thank you! ")
        print("========================")
        choices()
    if interest_input == "Complex Compound Interest":
        # Here we are going to allow the viwer to alter the time period instead of the initial amount so they can check that out 
        key()
        print("An example of complex compound interest is if you give 100 dollars away at 2% compounded interest monlthy for 10 years, then you would get 1 + .02/12 interest monlthy for 120 months which would be 100, 100.17, 100.51... 122.12")
        print("The equation is: A = P(1+r/n)^n*t")
        print("The explination behind this equation is quite simple. Instead of multiplying a result by 1.02 for an amount of years, we are multiplying a result by a smaller (1.0017) for many more mornths. The kicker in these complex compounding equations is that the more compounds there are (n) the more money you get out of it.")
        print("Now let's try this equation ourselves and test whether more compounds yield more money. Give me a compound count higher than 12 to compare the results for an initially 100 dollar investment with .05 interest compounded monthly for 10 years.")
        compounds_per_year = input()
        print(complex_compound_interest(compounds_per_year))
        print("As you can see if you put a number in larger than 12 you will be left with more money because more money was put into increasing amounts")
        print("You can continue learning about other interests by typing another type below or simply exit. Thank you! ")
        choices()
    if interest_input == "Continuous Interest":
        key()
        print("An example of continuous interest is when you compound infinately and everytime n gets bigger and bigger it somehow stops losing traction and ends up becoming eular's number = e")
        print("The equation is: A = P * e^rt")
        print("Now let's try this equation ourselves. Give me a starting amount for continuous interset for 10 years and 10%")
        continuous_interest_input = input()
        print(continuous_interest(continuous_interest_input))
        print("This is the amount of money you will have after 10 years with continuous interest of .10 with a starting amount of " + continuous_interest_input)
        print("You can continue learning about other interests by typing another type below or simply exit. Thank you! ")
        choices()

choices()

balls = "Hi"