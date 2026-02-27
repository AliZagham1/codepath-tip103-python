"""
Problem: Tiggerfy
Source: CodePath TIP-103

Description:
Remove the substrings "t", "i", "gg", and "er" from the given word.
The removal should be case insensitive.
Return the resulting string.

Time Complexity: O(n)
Space Complexity: O(n)
"""


def tiggerfy(word):
    result = ""
    i = 0

    while i < len(word):
        current_char = word[i].lower()
        next_two_chars = word[i:i+2].lower()

        # Remove multi-character patterns first
        if next_two_chars == "gg" or next_two_chars == "er":
            i += 2

        # Remove single characters
        elif current_char == "t" or current_char == "i":
            i += 1

        # Keep everything else
        else:
            result += word[i]
            i += 1

    return result


if __name__ == "__main__":
    # Test Case 1
    print(tiggerfy("Trigger"))   # Expected: "r"

    # Test Case 2
    print(tiggerfy("eggplant"))  # Expected: "eplan"

    # Test Case 3
    print(tiggerfy("Choir"))     # Expected: "Chor"