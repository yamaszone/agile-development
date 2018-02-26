import unittest
from ddt import ddt, data
from tdd.src import data_driven_test

@ddt
class test_data_driven_test(unittest.TestCase):

	@data("AA", "XR", "A", "ABCDEFGHIJKLMNOPQRSTUVXYZ")
	def test_foo_returns_true(self, word):
		self.assertTrue(data_driven_test.is_all_uppercase(word))

	@data("Az", "zR", "i", "abcedef", "ABCDEFGHiJKLMNOPQRSTUVXYZ")
	def test_foo_returns_false(self, word):
		self.assertFalse(data_driven_test.is_all_uppercase(word))
