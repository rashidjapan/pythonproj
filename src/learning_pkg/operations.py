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
