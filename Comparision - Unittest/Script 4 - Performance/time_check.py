import time
import unittest
import pytest

number_of_iterations = 10000
# Unittest example
class TestMath(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        pass
    
    @classmethod
    def tearDownClass(self):
        pass
    
    def test_time(self):
        for i in range(number_of_iterations):
            with self.subTest(i):
                self.assertEqual(0, i)


# Measure time for Unittest
start_time = time.time()
unittest.main(argv=[''], exit=False)
unittest_time = time.time() - start_time

# # Measure time for Pytest
# start_time = time.time()
# pytest.main(['-s'])
# pytest_time = time.time() - start_time

print(f"Time taken by unittest: {unittest_time} seconds")
# print(f"Time taken by pytest: {pytest_time} seconds")
