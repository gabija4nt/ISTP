import unittest

# Functions to test
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero.")
    return a / b

def reverse_string(s):
    return s[::-1]

def is_palindrome(s):
    return s == s[::-1]

def count_vowels(s):
    return sum(1 for char in s if char in 'aeiouAEIOU')

def find_max(lst):
    if not lst:
        return None
    return max(lst)

def find_min(lst):
    if not lst:
        return None
    return min(lst)

def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n - 1)

def fibonacci(n):
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    seq = [0, 1]
    for i in range(2, n):
        seq.append(seq[-1] + seq[-2])
    return seq

def is_even(n):
    return n % 2 == 0

def is_odd(n):
    return n % 2 != 0

def sort_list(lst):
    return sorted(lst)

def filter_odd_numbers(lst):
    return [num for num in lst if num % 2 != 0]

def filter_even_numbers(lst):
    return [num for num in lst if num % 2 == 0]

def to_uppercase(s):
    return s.upper()

def to_lowercase(s):
    return s.lower()

def square_number(n):
    return n * n

# Unit Test Class
class TestMyFunctions(unittest.TestCase):

    def test_add(self):
        self.assertEqual(add(2, 3), 5)
        self.assertEqual(add(-1, 1), 0)

    def test_subtract(self):
        self.assertEqual(subtract(5, 3), 2)
        self.assertEqual(subtract(-1, 1), -2)

    def test_multiply(self):
        self.assertEqual(multiply(3, 4), 12)
        self.assertEqual(multiply(-2, 3), -6)

    def test_divide(self):
        self.assertEqual(divide(6, 3), 2)
        self.assertRaises(ValueError, divide, 5, 0)

    def test_reverse_string(self):
        self.assertEqual(reverse_string('hello'), 'olleh')
        self.assertEqual(reverse_string(''), '')

    def test_is_palindrome(self):
        self.assertTrue(is_palindrome('madam'))
        self.assertFalse(is_palindrome('hello'))

    def test_count_vowels(self):
        self.assertEqual(count_vowels('hello world'), 3)
        self.assertEqual(count_vowels('rhythm'), 0)

    def test_find_max(self):
        self.assertEqual(find_max([1, 2, 3, 4]), 4)
        self.assertEqual(find_max([-1, -2, -3]), -1)
        self.assertIsNone(find_max([]))

    def test_find_min(self):
        self.assertEqual(find_min([1, 2, 3, 4]), 1)
        self.assertEqual(find_min([-1, -2, -3]), -3)
        self.assertIsNone(find_min([]))

    def test_factorial(self):
        self.assertEqual(factorial(5), 120)
        self.assertEqual(factorial(0), 1)

    def test_fibonacci(self):
        self.assertEqual(fibonacci(5), [0, 1, 1, 2, 3])
        self.assertEqual(fibonacci(1), [0])
        self.assertEqual(fibonacci(0), [])

    def test_is_even(self):
        self.assertTrue(is_even(4))
        self.assertFalse(is_even(3))

    def test_is_odd(self):
        self.assertFalse(is_odd(4))
        self.assertTrue(is_odd(3))

    def test_sort_list(self):
        self.assertEqual(sort_list([3, 1, 4, 2]), [1, 2, 3, 4])
        self.assertEqual(sort_list([-3, -1, 2]), [-3, -1, 2])

    def test_filter_odd_numbers(self):
        self.assertEqual(filter_odd_numbers([1, 2, 3, 4]), [1, 3])
        self.assertEqual(filter_odd_numbers([2, 4, 6]), [])

    def test_filter_even_numbers(self):
        self.assertEqual(filter_even_numbers([1, 2, 3, 4]), [2, 4])
        self.assertEqual(filter_even_numbers([1, 3, 5]), [])

    def test_to_uppercase(self):
        self.assertEqual(to_uppercase('hello'), 'HELLO')
        self.assertEqual(to_uppercase(''), '')

    def test_to_lowercase(self):
        self.assertEqual(to_lowercase('HELLO'), 'hello')
        self.assertEqual(to_lowercase(''), '')

    def test_square_number(self):
        self.assertEqual(square_number(3), 9)
        self.assertEqual(square_number(-4), 16)

if __name__ == '__main__':
    unittest.main()
