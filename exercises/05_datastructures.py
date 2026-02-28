"""Exercise 05: Basic data structures
Run: python exercises/05_datastructures.py
"""


def show_examples():
    # list: ordered, mutable, allows duplicates
    lst = [1, 2, 3, 2]
    print("list example", lst)

    # dict: key->value mapping, keys must be hashable
    dct = {"a": 1, "b": 2}
    print("dict example", dct)

    # set: unordered collection of unique items
    st = {1, 2, 3, 2}
    print("set example", st)

    # tuple: ordered, immutable sequence
    tpl = (1, 2, 3)
    print("tuple example", tpl)


if __name__ == "__main__":
    show_examples()
