"""Simple runner script to demonstrate usage of functions in `operations.py`."""

# support both package and script execution by importing the module itself
try:
    from . import operations as ops
except ImportError:  # script mode
    import os, sys
    pkg_root = os.path.dirname(os.path.dirname(__file__))
    if pkg_root not in sys.path:
        sys.path.insert(0, pkg_root)
    import learning_pkg.operations as ops

# funcs can now be accessed via ops.square, ops.cube, ops.addlist


def main1() -> None:
    for i in range(1, 6):
        print(f"{i} squared is {ops.square(i)} and cubed is {ops.cube(i)}")

def main2() -> None:
    sum_result = ops.addlist([1, 2, 3, 4, 5])
    print(f"Sum of [1, 2, 3, 4, 5] is {sum_result}")        

def main() -> None:
    datastructure_list_result = ops.handle_datastructire([1, 2, 3, 4, 5])
    datastructure_dict_result = ops.handle_datastructire({"a": 1, "b": 2, "c": 3})
    datastructure_set_result = ops.handle_datastructire({1, 2, 3, 4, 5})
    datastructure_tuple_result = ops.handle_datastructire((1, 2, 3, 4, 5))
    print(f"Summary of the list data structure: {datastructure_list_result}")
    print(f"Summary of the dict data structure: {datastructure_dict_result}")
    print(f"Summary of the set data structure: {datastructure_set_result}")
    print(f"Summary of the tuple data structure: {datastructure_tuple_result}")        


if __name__ == "__main__":
    main()
