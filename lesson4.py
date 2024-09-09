import random

# Generates random number between 1-100
random_number = random.randint(1,100)

# Prints random integer 
print(random_number, type(random_number))

# Casts random_number into a float data type 
float_number = float(random_number)
print(random_number, type(float_number))

# Casts random_number into a complex data type
complex_number = complex(random_number)
print(complex_number, type(complex_number))
