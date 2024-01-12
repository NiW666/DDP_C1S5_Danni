def morse_translator(text):
    # Morse code mapping
    morse_code_dict = {
        "A": ".-",
        "B": "-...",
        "C": "-.-.",
        "D": "-..",
        "E": ".",
        "F": "..-.",
        "G": "--.",
        "H": "....",
        "I": "..",
        "J": ".---",
        "K": "-.-",
        "L": ".-..",
        "M": "--",
        "N": "-.",
        "O": "---",
        "P": ".--.",
        "Q": "--.-",
        "R": ".-.",
        "S": "...",
        "T": "-",
        "U": "..-",
        "V": "...-",
        "W": ".--",
        "X": "-..-",
        "Y": "-.--",
        "Z": "--..",
    }

    # Convert the input text to uppercase for case-insensitivity
    text = text.upper()

    morse_code_list = []
    for i in text:
        # Check if the character is alphabetic
        if i.isalpha():
            # Translate the alphabetic character to Morse code
            morse_code_list.append(morse_code_dict[i])
        elif i == " ":
            # Add a forward slash for space between words
            morse_code_list.append("/")
    
    # Join the Morse code elements and return the result
    return " ".join(morse_code_list)

# Test cases
print(morse_translator("HELLO WORLD"))  # Output: ".... . .-.. .-.. --- / .-- --- .-. .-.. -.."
print(morse_translator("Python"))  # Output: ".--. -.-- - .... --- -."
print(morse_translator("Morse Code"))  # Output: "-- --- .-. ... . / -.-. --- -.. ."