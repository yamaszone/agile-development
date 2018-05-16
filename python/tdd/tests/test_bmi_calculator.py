# See: http://ddt.readthedocs.io/en/latest/example.html
import unittest
from ddt import ddt, data, unpack
from tdd.src import bmi_calculator

@ddt
class test_bmi_calculator(unittest.TestCase):

  def test_calculate_returns_weight_group(self):
    self.assertEqual('Underweight', bmi_calculator.calculate(weight=120, height=72))

  @unpack
  @data(
    {'age_group': 'Underweight', 'height': 65, 'weight': 80},
    {'age_group': 'Normal', 'height': 72, 'weight': 165}
  )
  def test_calculate_returns_weight_group_v2(self, age_group, weight, height):
    self.assertEqual(age_group, bmi_calculator.calculate(weight, height))
