"""
Correction script for the cryptography exercise.
"""

import main

def test_brute_force():
    cipher_text = "qeb nrfzh yoltk clu grjmp lsbo qeb ixwv ald"
    expected = "the quick brown fox jumps over the lazy dog"

    try:
        decrypted_options = main.brute_force_caesar(cipher_text)

        # Validate if expected result is in decrypted options
        correct_shift = None
        for shift, text in decrypted_options.items():
            if text == expected:
                correct_shift = shift
                break

        if correct_shift is None:
            print(f"❌ Test failed for: {cipher_text}")
            print(f"   Expected: '{expected}'")
            print(f"   Decrypted Options: {list(decrypted_options.values())[:5]}... (showing first 5)")
        else:
            print(f"✅ Test passed for: {cipher_text} (Correct shift: {correct_shift})")
    except Exception as e:
        print(f"❌ Test failed for: {cipher_text}")
        print(f"   Error: {e}\n")

if __name__ == "__main__":
    print("🔍 Starting test...\n")
    test_brute_force()
    print("\n✅ Test completed.")
