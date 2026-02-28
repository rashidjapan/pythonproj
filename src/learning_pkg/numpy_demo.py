"""Simple NumPy learning script. Run as module or script."""

try:
    import numpy as np
except ImportError:
    np = None


def main() -> None:
    if np is None:
        print("numpy is not installed. install with 'pip install numpy'")
        return
    a = np.arange(10)
    print("array:", a)
    print("mean:", a.mean())
    print("reshape 2x5:\n", a.reshape((2, 5)))


if __name__ == "__main__":
    main()
