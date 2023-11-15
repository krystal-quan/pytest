import timeit

def time_unittest():
    return timeit.timeit('import unittest; unittest.main()', number=1000, globals=globals())

def time_pytest():
    return timeit.timeit('import pytest; pytest.main()', number=1000, globals=globals())

print(f"Time taken by unittest: {time_unittest()} seconds")
print(f"Time taken by pytest: {time_pytest()} seconds")
