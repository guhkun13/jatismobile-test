from satu import find_fewest_bottle
import unittest

class TestFindFewestBottle(unittest.TestCase):

  global err_msg_positive_prime_number
  global err_msg_litter_milk_outside_range
  MIN_CAP = 0
  MAX_CAP = 30

  MIN_LITTER = 100
  MAX_LITTER = 1000000

  err_msg_positive_prime_number     = f"value inputted should be positive and prime number : {MIN_CAP} < x < {MAX_CAP}"
  err_msg_litter_milk_outside_range = f"value milk litter should be : {MIN_LITTER} < x < {MAX_LITTER}"

  def test_ok(self):
    func = find_fewest_bottle(5,7,11,100)
    expected_result = 10
    self.assertEqual(func, expected_result)
  
  def test_ok_2(self):
    func = find_fewest_bottle(11,5,7,100)
    expected_result = 10
    self.assertEqual(func, expected_result)
  
  def test_err_negative_capacity_b1(self):
    func = find_fewest_bottle(-5,7,11,100)
    expected_result = err_msg_positive_prime_number

    self.assertEqual(func, expected_result)
  
  def test_err_negative_capacity_b2(self):
    func = find_fewest_bottle(5,-7,11,100)
    expected_result = err_msg_positive_prime_number

    self.assertEqual(func, expected_result)

  def test_err_negative_capacity_b3(self):
    func = find_fewest_bottle(5,7,-11,100)
    expected_result = err_msg_positive_prime_number

    self.assertEqual(func, expected_result)

  def test_err_over_capacity_b1(self):
    func = find_fewest_bottle(31,7,11,100)
    expected_result = err_msg_positive_prime_number

    self.assertEqual(func, expected_result)
  
  def test_err_over_capacity_b2(self):
    func = find_fewest_bottle(3,71,11,100)
    expected_result = err_msg_positive_prime_number

    self.assertEqual(func, expected_result)
  
  def test_err_over_capacity_b3(self):
    func = find_fewest_bottle(3,11,81,100)
    expected_result = err_msg_positive_prime_number

    self.assertEqual(func, expected_result)
  
  def test_err_not_prime_number_b1(self):
    func = find_fewest_bottle(6,11,81,100)
    expected_result = err_msg_positive_prime_number

    self.assertEqual(func, expected_result)
  
  def test_err_not_prime_number_b2(self):
    func = find_fewest_bottle(5,12,31,100)
    expected_result = err_msg_positive_prime_number

    self.assertEqual(func, expected_result)
  
  def test_err_not_prime_number_b3(self):
    func = find_fewest_bottle(5,13,30,100)
    expected_result = err_msg_positive_prime_number

    self.assertEqual(func, expected_result)
  
  def test_err_not_integer_b1(self):
    func = find_fewest_bottle(5.51,13,30,100)
    expected_result = err_msg_positive_prime_number

    self.assertEqual(func, expected_result)
  
  
  # test for X = 100 < X < 1000000
  def test_err_litter_zero(self):
    func = find_fewest_bottle(5,13,23,0)
    expected_result = err_msg_litter_milk_outside_range

    self.assertEqual(func, expected_result)
  
  def test_err_litter_negative(self):
    func = find_fewest_bottle(5,13,23,-10)
    expected_result = err_msg_litter_milk_outside_range

    self.assertEqual(func, expected_result)
  
  def test_err_litter_under(self):
    func = find_fewest_bottle(5,13,23,10)
    expected_result = err_msg_litter_milk_outside_range

    self.assertEqual(func, expected_result)
  
  def test_err_litter_upper(self):
    func = find_fewest_bottle(5,13,23,2000000)
    expected_result = err_msg_litter_milk_outside_range

    self.assertEqual(func, expected_result)
  
  def test_err_not_integer(self):
    print ("test_err_not_integer")
    func = find_fewest_bottle(13,3,2,110.8)
    expected_result = err_msg_litter_milk_outside_range

    self.assertEqual(func, expected_result)

if __name__ == '__main__':
  unittest.main()