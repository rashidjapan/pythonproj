"""Exercise 03: Collections and comprehensions
Run: python exercises/03_collections.py
"""


def common_elements(a, b):
    return list(set(a) & set(b))


if __name__ == "__main__":
    a = [1, 2, 3, 4]
    b = [3, 4, 5, 6]
    print(common_elements(a, b))
