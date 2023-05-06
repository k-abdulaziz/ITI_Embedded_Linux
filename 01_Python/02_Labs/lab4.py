# Ask the user to enter three sensor values and store them in variables
Sensor1 = int(input("Enter Sensor1: "))
Sensor2 = int(input("Enter Sensor2: "))
Sensor3 = int(input("Enter Sensor3: "))

# Create a list with the three sensor values
myList = [Sensor1, Sensor2, Sensor3]

# Create a tuple with the three sensor values
myTuple = (Sensor1, Sensor2, Sensor3)

# Create a dictionary with keys "Sensor1", "Sensor2", and "Sensor3",
# and values corresponding to the sensor values entered by the user
myDict = {
 "Sensor1": Sensor1,
 "Sensor2": Sensor2,
 "Sensor3": Sensor3
}	

# Print the list, tuple, and dictionary
print(myList)
print(myTuple)
print(myDict)


