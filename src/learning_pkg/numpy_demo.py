"""Simple NumPy learning script. Run as module or script."""

try:
    import numpy as np
except ImportError:
    np = None


def main() -> None:
    if np is None:
        print("numpy is not installed. install with 'pip install numpy'")
        return
    a = np.arange(10,20,30)
    print("array:", a)
    print("mean:", a.mean())


if __name__ == "__main__":
    main()
