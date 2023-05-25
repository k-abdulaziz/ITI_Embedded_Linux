# Prompt the user to enter their name, university, and age
x = input("Enter Name: ")
y = input("Enter University: ")
z = input("Enter Age: ")

# Open a file called "info.txt" in write mode and write the user's information
f1 = open("info.txt", "w")
f1.write("My Name is {}\nMy University is {}\nMy Age is {}".format(x, y, z))

# Close the file after writing
f1.close()

# Open the file in read mode and print its contents
f1 = open("info.txt", "r")
print(f1.read())

# Close the file after reading
f1.close()
