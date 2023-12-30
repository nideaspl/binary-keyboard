import keyboard
import pyautogui

# Initialize variables
binary_sequence = ""
CHARACTER_LENGTH = 8

# Function to convert binary to ASCII and type it
def convert_and_type(binary_sequence):
    try:
        # Convert binary to ASCII
        char_code = int(binary_sequence, 2)
        character = chr(char_code)

        # Type the character at the current cursor position
        pyautogui.typewrite(character)

        # Print the conversion result
        print(f"Converted: {character}   Binary Sequence: {binary_sequence}")
    except ValueError:
        print("Invalid binary sequence")

# Main loop to continuously listen to keyboard input
while True:
    try:
        # Get the last key pressed
        event = keyboard.read_event(suppress=True)

        # Check if it's a key press event
        if event.event_type == keyboard.KEY_DOWN:
            key = event.name

            # Check if the key is 0 or 1
            if key in ['0', '1']:
                binary_sequence += key
                print(f"Entered: {key}   Binary Sequence: {binary_sequence}")

                # Check if the binary sequence is complete
                if len(binary_sequence) == CHARACTER_LENGTH:
                    convert_and_type(binary_sequence)

                    # Reset the binary sequence after every 8 bits
                    binary_sequence = ""

            # Clear the keyboard buffer
            keyboard.read_event(suppress=True)

    except keyboard.KeyboardInterrupt:
        break
