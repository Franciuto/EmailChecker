import re
import sys

# Read from file
file_location = input("File location: ")

# Regex to check if the filename ends with .txt
file_check = r'.*\.txt$'

# Regex to validate the email syntax
regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'

# If the input filename doesn't end with .txt, prompt the user to enter it again
while (not re.fullmatch(file_check, file_location)):
    file_location = input("Invalid input\nFile location:")

# List declarations
linelist = []       # List to hold the lines from the file
wrongmails = []     # List to store invalid emails

# Read the file lines and assign them to linelist
try:
    file = open(file_location , 'r')
    f = file.readlines()
    for line in f:
        linelist.append(line.strip())

# Exit the program if the file is not found
except FileNotFoundError:
        print("File not found")
        sys.exit()

# Initialize variables for counting correct and wrong emails
c = 0   # Counts the correct emails in the file
w = 0   # Counts the wrong emails in the file

# Check if the emails are valid
for line in linelist:
    if re.match(regex, line):
        c += 1  # Increment the correct email counter
    else:
        wrongmails.append(line)  # Add invalid email to the list
        w += 1  # Increment the wrong email counter

# Print the statistics of the analysis to the shell
print(f"There are {c} valid emails and {w} invalid emails.")
if wrongmails:
    print("The invalid emails are:")
    for i in wrongmails:
        print(i)

# Ask the user if they want to save the result to a file
saveastext = input('Enter the output filename to save the results to a .txt file\nOtherwise, type "exit" to quit: ')

# If the user doesn't type "exit", save the results to a file
if saveastext != "exit":
    filename = saveastext + ".txt"
    # Create the file with the provided name and save the results there
    with open(filename, "w") as file:
        file.write(f"There are {c} valid emails and {w} invalid emails.\n")
        if wrongmails:
            file.write("The invalid emails are:\n\n")
            for i in wrongmails:
                file.write(i + "\n")
    print(f"Results saved in '{saveastext}.txt'")