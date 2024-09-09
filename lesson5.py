string = input("Enter a string: ")
print("""Option 1: Convert the string to uppercase
Option 2: Convert the string to lowercase
Option 3: Slice the string from a start index to an end index
Option 4: Calculate the length of the string
Option 5: Loop through each character in the string and display it on a new line""")

# Perform the selected string manipulation
choice = int(input("Enter your choice: "))

if choice == 1:
    print("Uppercase: ", string.upper())
elif choice == 2:
    print("Lowercase: ", string.lower())
elif choice == 3:
    start = int(input("Enter start index: "))
    end = int(input("Enter end value: "))
    print("Sliced string: ", string[start:end])
elif choice == 4:
    print("Length: ", len(string))
elif choice == 5:
    print("Characters: ")
    for char in string:
        print(char)
else:
    print("Invalid Choice")