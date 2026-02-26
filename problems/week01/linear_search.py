"""
Problem: Linear Search
Description:
Return the first index of target in items.
Return -1 if target is not found.
"""

def linear_search(items, target):
    for index, item in enumerate(items):
        if item == target:
            return index
        
    return -1
        


if __name__ == "__main__":
    # test cases
    items1 = ['haycorn', 'haycorn', 'haycorn', 'hunny', 'haycorn']
    print(linear_search(items1, 'hunny'))  # expected: 3

    items2 = ['bed', 'blue jacket', 'red shirt', 'hunny']
    print(linear_search(items2, 'red balloon'))  # expected: -1