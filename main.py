# All file paths
NAMES_FILE_PATH = "input/Names/invited_names.txt"
LETTER_FILE_PATH = "input/Letters/starting_letter.txt"
PLACEHOLDER_1 = "[name]"
PLACEHOLDER_2 = "Angela"

# TODO : 1 Accessing the names and removing the extra spaces
# Reading the names and storing in the list
names = open(file=NAMES_FILE_PATH, mode='r')
raw_name_List = list(names)  # List to store the names

# Removing extra space using strip()
name_list = [name.strip() for name in raw_name_List]

# TODO : 2 Accessing the invited_names file and replacing the [name] with actual name holder in the starting_letter file and making copies
# Accessing the sample letter
with open(file=LETTER_FILE_PATH, mode='r') as file:
    letter_sample = file.read()  # letter sample

# Using for loop to replace the old words and creating copies
for name in name_list:
    user_data = letter_sample.replace(f"{PLACEHOLDER_1}", f"{name}").replace(f"{PLACEHOLDER_2}", "Abdullah Khurram")

    # Creating a copy
    with open(file=f"Output/ReadyToSend/{name}_letter.txt", mode='w') as file:
        file.write(user_data)