"""
Mission: Decrypt the password to unlock a confidential file.

Story:
Cybercriminals have encrypted the password needed to access a sensitive file using Caesar Cipher.
Your task is to decrypt this password by testing all possible shifts (1 to 25).

Instructions:
1. Implement the `brute_force_caesar` function below. It should test all possible shifts
   and return all the decryption options.
2. Once you've completed the function, run this script to see your results or `correction.py` to validate your solution.

Encrypted password:
- "qeb nrfzh yoltk clu grjmp lsbo qeb ixwv ald"

Good luck, agent!
"""

def brute_force_caesar(cipher_text):
    """
    Decrypts a text encrypted using Caesar Cipher by testing all possible shifts.
    
    Args:
        cipher_text (str): The encrypted text.
    
    Returns:
        dict: A dictionary where keys are shifts (1-25) and values are the decrypted text options.
    """
    # TODO: Implement this function
    pass


if __name__ == "__main__":
    # Test encrypted password
    cipher_text = "qeb nrfzh yoltk clu grjmp lsbo qeb ixwv ald"

    print(f"Decrypting: {cipher_text}")
    options = brute_force_caesar(cipher_text)
    if options:  # Only print if the function is implemented
        for shift, text in options.items():
            print(f"Shift {shift}: {text}")
    else:
        print("Function not implemented yet. Complete the 'brute_force_caesar' function.")
