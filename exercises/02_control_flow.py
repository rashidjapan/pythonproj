"""Exercise 02: Control flow and functions
Run: python exercises/02_control_flow.py
"""


def fizzbuzz(n: int):
    for i in range(1, n+1):
        if i % 15 == 0:
            print("FizzBuzz")
        elif i % 3 == 0:
            print("Fizz")
        elif i % 5 == 0:
            print("Buzz")
        else:
            print(i)


if __name__ == "__main__":
    fizzbuzz(30)
