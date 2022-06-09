from main import count_and_sort as myfunc
import  unittest

class MainTestCase(unittest.TestCase):

  def count_result(self, char, list_str):
    return list_str[char]

  def test_simple_ok(self):
    randstr = "gfedcba"
    onestr, list_str_count = myfunc(randstr)

    sorted_str = "abcdefg"
    self.assertEqual(onestr, sorted_str)

    count_a = 1    
    self.assertEqual(count_a, self.count_result('a', list_str_count))

  def test_double_xx(self):
      randstr = "cbaxx"
      onestr, list_str_count = myfunc(randstr)

      sorted_str = "abcxx"
      self.assertEqual(onestr, sorted_str)

      count_x = 2    
      self.assertEqual(count_x, self.count_result('x', list_str_count))

  def test_with_space(self):
      randstr = "cba s"
      onestr, list_str_count = myfunc(randstr)

      sorted_str = " abcs"
      self.assertEqual(onestr, sorted_str)

      count_x = 1
      self.assertEqual(count_x, self.count_result(' ', list_str_count))

if __name__ == '__main__':
  unittest.main()
  


