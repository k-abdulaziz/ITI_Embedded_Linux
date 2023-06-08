#!/bin/bash

user="admin"  # Set the expected username
password="admin"  # Set the expected password

read -p "Please enter username: " user_input  # Prompt the user to enter a username

if [[ "$user_input" == "$user" ]]; then  # Check if the entered username matches the expected username
    read -p "Please enter password: " password_input  # Prompt the user to enter a password
    if [[ "$password_input" == "$password" ]]; then  # Check if the entered password matches the expected password
        echo "Welcome $user"  # Display a welcome message if both username and password are correct
    else
        echo "Incorrect password!"  # Display an error message if the entered password is incorrect
        exit 1  # Exit the script with an error code of 1
    fi
else
    echo "Invalid username!"  # Display an error message if the entered username is incorrect
    exit 1  # Exit the script with an error code of 1
fi
