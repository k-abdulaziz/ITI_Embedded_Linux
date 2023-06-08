#!/bin/bash

read -p "Enter first number: " Num1  # Prompt the user to enter the first number
read -p "Enter second number: " Num2  # Prompt the user to enter the second number
read -p "Select an operation (+, -, *, /): " Operation  # Prompt the user to select an operation

if [ "$Operation" == "+" ]; then  # Check if the operation is addition
    Result=$(echo "$Num1 + $Num2" | bc)  # Perform addition and store the result in the variable Result
elif [ "$Operation" == "-" ]; then  # Check if the operation is subtraction
    Result=$(echo "$Num1 - $Num2" | bc)  # Perform subtraction and store the result in the variable Result
elif [ "$Operation" == "*" ]; then  # Check if the operation is multiplication
    Result=$(echo "$Num1 * $Num2" | bc)  # Perform multiplication and store the result in the variable Result
elif [ "$Operation" == "/" ]; then  # Check if the operation is division
    Result=$(echo "$Num1 / $Num2" | bc)  # Perform division and store the result in the variable Result
else  # If none of the valid operations are selected
    echo "Invalid operation selected!"  # Display an error message
    exit 10  # Exit the script with an error code 10
fi

echo "The result of $Num1 $Operation $Num2 is: $Result"  # Display the calculated result to the user
