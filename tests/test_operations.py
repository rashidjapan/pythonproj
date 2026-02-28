from src.learning_pkg import operations


def test_square():
    print('operations file in test:', operations.__file__)
    print('operations content in test:')
    with open(operations.__file__, 'r') as f:
        print(f.read())
    assert operations.square(3) == 9


def test_cube():
    assert operations.cube(2) == 8


def test_addlist():
    assert operations.addlist([1, 2, 3]) == 6
