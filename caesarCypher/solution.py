"""
Solution script for the cryptography exercise.
"""

def brute_force_caesar(cipher_text):
    """
    Decrypts a text encrypted using Caesar Cipher by testing all possible shifts.
    
    Args:
        cipher_text (str): The encrypted text.
    
    Returns:
        dict: A dictionary where keys are shifts (1-25) and values are the decrypted text options.
    """
    decrypted_options = {}
    
    for shift in range(1, 26):  # Test all shifts from 1 to 25
        decrypted_text = ""
        for char in cipher_text:
            if char.isalpha():  # Only decrypt alphabetic characters
                shifted = ord(char) - shift  # Decrypt with a left shift
                if char.islower():
                    if shifted < ord('a'):  # Wrap around for lowercase
                        shifted += 26
                elif char.isupper():
                    if shifted < ord('A'):  # Wrap around for uppercase
                        shifted += 26
                decrypted_text += chr(shifted)
            else:  # Preserve non-alphabetic characters
                decrypted_text += char
        decrypted_options[shift] = decrypted_text

    return decrypted_options


if __name__ == "__main__":
    # Test encrypted password
    cipher_text = "qeb nrfzh yoltk clu grjmp lsbo qeb ixwv ald"

    print(f"Decrypting: {cipher_text}")
    options = brute_force_caesar(cipher_text)
    for shift, text in options.items():
        print(f"Shift {shift}: {text}")
