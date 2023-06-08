#!/bin/bash

read -p "Enter first number: " NUM1  # Prompt the user to enter the first number
read -p "Enter second number: " NUM2  # Prompt the user to enter the second number

touch "calc_file"  # Create a file named "calc_file"

RESULT_FILE="calc_file"  # Store the file name in the variable RESULT_FILE

echo $(echo "$NUM1 + $NUM2" | bc) >> "$RESULT_FILE"  # Calculate the sum of NUM1 and NUM2, then append it to the RESULT_FILE
echo $(echo "$NUM1 - $NUM2" | bc) >> "$RESULT_FILE"  # Calculate the difference of NUM1 and NUM2, then append it to the RESULT_FILE
echo $(echo "$NUM1 * $NUM2" | bc) >> "$RESULT_FILE"  # Calculate the product of NUM1 and NUM2, then append it to the RESULT_FILE
echo $(echo "$NUM1 / $NUM2" | bc) >> "$RESULT_FILE"  # Calculate the division of NUM1 by NUM2, then append it to the RESULT_FILE

echo "Results have been stored in $RESULT_FILE."  # Notify the user that the results have been stored in the RESULT_FILE.
