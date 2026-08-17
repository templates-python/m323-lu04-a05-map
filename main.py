"""Verdoppeln der Elemente in einer Liste.

Aufgabenstellung: https://wiki.bzz.ch/modul/m323/learningunits/lu04/aufgaben/map1
"""

def double_elements(numbers):
    """
    Double each element in the list using the map function.
    Args:
    - numbers (list): List of numbers to be doubled.
    Returns:
    - list: List of doubled numbers.
    """
    # Your code here
    return list(map(lambda x: x * 2, numbers))


if __name__ == '__main__':
    demo_numbers = [1, 2, 3, 4, 5]
    doubled_list = double_elements(demo_numbers)
    print(doubled_list)
