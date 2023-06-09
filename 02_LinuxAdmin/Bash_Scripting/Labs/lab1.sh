#!/bin/bash
# Script: lab1.sh
# Description: This script prompts the user to enter their personal information and stores it in a file.

# Prompt the user to enter their name
read -p "What's Your Name?: " USER_NAME
echo "Hello $USER_NAME"  # Greet the user with their name

# Notify the user about the file creation
echo "I will create a file called ${USER_NAME}_file"

# Create a file with the user's name
touch "${USER_NAME}_file"

# Append the user's name to the file
echo "Name: $USER_NAME" >> "${USER_NAME}_file"

# Prompt the user to enter their university
read -p "Enter your university: " UNIVERSITY
echo "University: $UNIVERSITY" >> "${USER_NAME}_file"  # Append the university to the file

# Prompt the user to enter their age
read -p "Enter your age: " AGE
echo "Age: $AGE" >> "${USER_NAME}_file"  # Append the age to the file

# Prompt the user to enter their location
read -p "Where are you from?: " LOCATION
echo "Location: $LOCATION" >> "${USER_NAME}_file"  # Append the location to the file

# Notify the user about the successful storage of data in the file
echo "Data stored in ${USER_NAME}_file."
