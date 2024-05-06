# Invitation Letter Generator

This Python script automates the process of generating personalized invitation letters for multiple recipients.

## Usage

1. **Prepare Input Files:**
   - Create a file named `invited_names.txt` in the `input/Names` directory.
   - List the names of the individuals you want to invite, with each name on a new line.

2. **Customize Letter Template:**
   - Customize the invitation letter template by editing the `starting_letter.txt` file in the `input/Letters` directory.
   - Replace the `[name]` placeholder with the desired name of the recipient.

3. **Run the Script:**
   - Execute the `main.py` script.
   - The script will read the names from `invited_names.txt`, replace the placeholders in the letter template, and generate personalized invitation letters.
   - The generated letters will be saved in the `Output/ReadyToSend` directory as individual files for each recipient.
