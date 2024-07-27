# Bruce Provencher
# 13 AUG 20XX
# Building Python F-Strings 

# How do you create a string in Python?
car1 = "Chevrolet Malibu"
car2 = "Honda Accord"
mileage = 6

# Is the value on the next line of code an integer or a floating-point number (AKA a float)?
down_payment = 2500.0000000

# Predict the output
print(car2)
print(down_payment)

# Predict the output
# How is the f-string set up differently in the examples below?
print(f'Last Saturday, I went to two car dealers and test drove a {car1} and a {car2}.')
print(f"I needed ${down_payment:,.2f} for a down payment on the {car2}, which had only {mileage} miles on it.")
