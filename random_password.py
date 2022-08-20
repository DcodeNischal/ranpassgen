import random  # Import the random module
import string  # Import the string module

# Taking length of password
len = int(input('\nEnter the length of password: '))

# Checking if length is greater than 8
if len >= 8:
    lowercase = string.ascii_lowercase  # lowercase letters
    uppercase = string.ascii_uppercase  # uppercase letters
    numbers = string.digits  # numbers
    special = string.punctuation  # special characters
    # you can easily get access to all the characters by the help of string library

    # combining all the characters
    combination = lowercase+uppercase+numbers+special

    # randomly selecting characters from the combination

    temporary = random.sample(combination, len)
    # this stores the randomly selected characters in temporary variable as an array

    password = "".join(temporary)
    # join function joins the elements of an array into a string

    print(f"The password is {password}")
    print("Please note down this password. This program does not store passwords in any database.")

else:
    print("The length must be greater than 8. Please re-run the program with right value.")
    # if length is less than 8, it will print the message
    SystemExit
