
Python Project Repository

This repository houses a collection of Python projects and exercises. Below is an overview of the project structure:

Folders

1. Portfolio
   Description: This folder contains various programming exercises and practice questions from week 1 to 7.

   Contents: A collection of Python code snippets and small projects showcasing different programming concepts.

2. Task1
   Description:This GitHub repository contains a simple Python script for calculating the total price of pizza orders.The script prompts the user for input regarding the
                        number of pizzas, delivery requirements, whether it's Tuesday, and if the customer used an app. Based on this input, it calculates the total price, applying
                        discounts for Tuesday orders and app users.

   Contents: This Python script includes two main functions:
                      get_user_input(): Takes user input for pizza order details, handling exceptions for invalid input.
                      calculate_total_price(): Computes the total price considering the number of pizzas, delivery cost, Tuesday discount, 
                      and app discount.
                      The script then prints a summary, including any applicable discounts and the final total price
3. Task2

   Description:This contains a simple Python script for analyzing a cat shelter log file. The script calculates various statistics related                  to cat visits, including the number of visits, total time spent by the correct cat, average visit length, and more.

    contents:The main Python script that reads a cat shelter log file and performs the analysis.
             Uses descriptive variable names to enhance code readability.
             Prints insightful information about cat visits, intruder encounters, and visit durations.
   
4. Task3

     Description:The main Python script that includes functions for user management, such as adding users, changing passwords, deleting                       users, and logging in.The script interacts with a 'passwd.txt' file to store user information securely.
                 Utilizes getpass for secure password input.

     Contents:This Python script for user management includes several functions for handling user-related operations:
               add_user(username, real_name, password):Checks for existing usernames and adds a new user to the 'passwd.txt' file if the 
                  chosen username is unique.
                  Prints a success message if the user is created; otherwise, displays an error message.
               check_existing_username(username):Checks if a given username already exists in the 'passwd.txt' file.
                  Returns True if the username exists; otherwise, returns False.
               change_password(username, current_password, new_password):Changes the password for a given user if the provided current                          password matches the stored password in the 'passwd.txt' file.Prints a success message if the password is changed;                           otherwise, indicates that the user was not found or the current password is incorrect.
               delete_user(username):Deletes a user from the 'passwd.txt' file based on the provided username.
                   Prints a success message if the user is deleted; otherwise, indicates that the user was not found.
               login(username, password):Validates user credentials by checking the 'passwd.txt' file. Grants access if the username and 
                password match an entry.Prints an "Access granted" message if access is allowed; otherwise, displays "Access denied."
               main():The main part of the script that interacts with the user to perform various user management operations.
                  Presents a menu allowing the user to choose operations like changing passwords, deleting users, logging in, or adding new 
                  users.


