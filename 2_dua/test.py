from main import find_minimum_cost_food
import unittest

class MyTestCase(unittest.TestCase):

  global err_msg_must_be_positive_number
  global CONST_TOTAL_CARBS_NEEDED
  CONST_TOTAL_CARBS_NEEDED = 400
  RICE_CALS = 28
  CORN_CALS = 21
  POTATO_CALS = 17

  err_msg_must_be_positive_number = "Price must be positive number below a hundred: 0 < x < 100"

  def test_ok(self):
    func = find_minimum_cost_food(CONST_TOTAL_CARBS_NEEDED, rice = 2.0, corn = 1.4, potato = 1.8)
    expected_result = 77

    self.assertEqual(func, expected_result)
  
  def test_ok_custom_total_carbs(self):
    func = find_minimum_cost_food(14, rice = 2.0, corn = 2.0, potato = 1.8)
    expected_result = 2

    self.assertEqual(func, expected_result)
  
  def test_ok_custom_total_item_needed_exactly_10(self):
    func = find_minimum_cost_food(70, rice = 2.0, corn = 1.4, potato = 1.8)
    expected_result = 10

    self.assertEqual(func, expected_result)
    
  def test_err_negative_price_rice(self):
    func = find_minimum_cost_food(CONST_TOTAL_CARBS_NEEDED, rice = -2.0, corn = 1.4, potato = 1.8)
    expected_result = err_msg_must_be_positive_number

    self.assertEqual(func, expected_result)
  
  def test_err_negative_price_corn(self):
    func = find_minimum_cost_food(CONST_TOTAL_CARBS_NEEDED, rice = 2.0, corn = -11.4, potato = 1.8)
    expected_result = err_msg_must_be_positive_number

    self.assertEqual(func, expected_result)
  
  def test_err_negative_price_potato(self):
    func = find_minimum_cost_food(CONST_TOTAL_CARBS_NEEDED, rice = 2.0, corn = 11.4, potato = -10.8)
    expected_result = err_msg_must_be_positive_number

    self.assertEqual(func, expected_result)

if __name__ == '__main__':
  unittest.main()