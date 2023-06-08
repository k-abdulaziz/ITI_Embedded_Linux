#!/bin/bash

read -p "Whats Your Name?: " USER_NAME  # Prompt the user to enter their name
echo "Hello $USER_NAME"  # Greet the user with their name
echo "I will create a file called ${USER_NAME}_file"  # Notify the user about the file creation
touch "${USER_NAME}_file"  # Create a file with the user's name

echo "Name: $USER_NAME" >> "${USER_NAME}_file"  # Append the user's name to the file

read -p "Enter your university: " UNIVERSITY  # Prompt the user to enter their university
echo "University: $UNIVERSITY" >> "${USER_NAME}_file"  # Append the university to the file

read -p "Enter your age: " AGE  # Prompt the user to enter their age
echo "Age: $AGE" >> "${USER_NAME}_file"  # Append the age to the file

read -p "Where are you from?: " LOCATION  # Prompt the user to enter their location
echo "Location: $LOCATION" >> "${USER_NAME}_file"  # Append the location to the file

echo "Data stored in ${USER_NAME}_file."  # Notify the user about the successful storage of data in the file.
