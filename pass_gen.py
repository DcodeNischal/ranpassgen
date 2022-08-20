import random
import string

choice = int(input("\nEnter 1 to generate a password or 2 to retrive saved password: "))

if choice==1:
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
        
        # saving the password in a file
        save = int(input("\nDo you want to save this password? 1 for yes, 2 for no: "))
        if save==1:
            #inserting keyword to retrive later
            keyword = input("\nEnter the keyword: ")
            # opening the file in append mode
            with open("pass.log", "a") as f:
                f.write("keyword = "+keyword+"\t"+"Password = "+password+"\n")
                print("\nPassword saved successfully.")

    else:
        print("The length must be greater than 8. Please re-run the program with right value.")
        # if length is less than 8, it will print the message
        SystemExit

else:
    #retrieving the password from the file
    keyword = input("\nEnter the keyword: ")
    # opening the file in read mode
    with open("pass.log", "r") as f:
        for line in f:
            if keyword in line:
            #if the keyword is found in the line, it will print the password
            #split splits the line into an array of words
                print(line.split("\t")[1])
                break
        else:
            print("\nPassword not found.")
            SystemExit