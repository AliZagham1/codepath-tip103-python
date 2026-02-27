"""
Problem: Final Value After Operations
Source: CodePath TIP-103
Description:
Tiger starts with tigger = 1.
Operations:
- "bouncy" and "flouncy" increment by 1
- "trouncy" and "pouncy" decrement by 1
Return the final value after all operations.

Time Complexity: O(n)
Space Complexity: O(1)
"""


def final_value_after_operations(operations):
    tigger = 1

    for operation in operations:
        if operation in ("bouncy", "flouncy"):
            tigger += 1
        elif operation in ("trouncy", "pouncy"):
            tigger -= 1

    return tigger


if __name__ == "__main__":
    # Test Case 1
    operations1 = ["trouncy", "flouncy", "flouncy"]
    print(final_value_after_operations(operations1))  # Expected: 2

    # Test Case 2
    operations2 = ["bouncy", "bouncy", "flouncy"]
    print(final_value_after_operations(operations2))  # Expected: 4