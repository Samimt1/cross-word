def character_frequency_count(input_string):
    # Create an empty dictionary to store the frequency of each character
    frequency = {}

    # Loop through each character in the input string
    for char in input_string:
        # If the character is already in the dictionary, increment its count
        if char in frequency:
            frequency[char] += 1
        # Otherwise, add the character to the dictionary with a count of 1
        else:
            frequency[char] = 1

    return frequency

# Read input from the user
input_string = input("Enter a string: ")
frequency_count = character_frequency_count(input_string)

# Print the frequency count
for char, count in frequency_count.items():
    print(f"{char}: {count}")