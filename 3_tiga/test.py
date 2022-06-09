from main import sum_even_and_odd_from_fib_number as myfunc
import  unittest

class MainTestCase(unittest.TestCase):

  global err_msg_must_positive_number
  global err_msg_must_in_range
  err_msg_must_positive_number = f"value inputted should be positive : X & Y > 0"
  err_msg_must_in_range = f"value N should be in range : 2 < N < 1000000"

  def test_ok(self):
    func = myfunc(2,3,3)
    expected_result = (2,8,3)

    self.assertEqual(func, expected_result)

  def test_ok_2(self):
    func = myfunc(1,2,5)
    expected_result = (10,9,5)

    self.assertEqual(func, expected_result)
  
  def test_X_zero(self):
    func = myfunc(0,3,3)
    expected_result = err_msg_must_positive_number

    self.assertEqual(func, expected_result)

  def test_Y_zero(self):
    func = myfunc(2,0,3)
    expected_result = err_msg_must_positive_number

    self.assertEqual(func, expected_result)

  def test_X_negative(self):
    func = myfunc(-2,3,3)
    expected_result = err_msg_must_positive_number

    self.assertEqual(func, expected_result)

  def test_Y_negative(self):
      func = myfunc(2,-3,3)
      expected_result = err_msg_must_positive_number

      self.assertEqual(func, expected_result)

  def test_N_negative(self):
      func = myfunc(2,3,-3)
      expected_result = err_msg_must_in_range

      self.assertEqual(func, expected_result)

  def test_N_lte_1(self):
      func = myfunc(2,3,1)
      expected_result = err_msg_must_in_range

      self.assertEqual(func, expected_result)

if __name__ == '__main__':
  unittest.main()
  
