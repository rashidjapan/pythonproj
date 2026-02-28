"""Module holding reusable functions for the learning package."""

def square(x: int) -> int:
    """Return the square of an integer."""
    return x * x


def cube(x: int) -> int:
    """Return the cube of an integer."""
    return x * x * x

def addlist(nums: list[int]) -> int:
    """Return the sum of a list of integers."""
    return sum(nums)    

def handle_datastructire(data):
    """Example function to demonstrate handling of different data structures."""
    if isinstance(data, list):
        return [x * 2 for x in data]
    elif isinstance(data, dict):
        return {k: v * 2 for k, v in data.items()}
    elif isinstance(data, set):
        return {x * 2 for x in data}
    elif isinstance(data, tuple):
        return tuple(x * 2 for x in data)
    else:
        raise ValueError("Unsupported data type")
