from main import found_probability_for_sum as myfunc
import  unittest

DICES = 3
TOTAL_EVENT = 6**DICES

class MainTestCase(unittest.TestCase):

  global err_msg_outside_range
  err_msg_outside_range = "your inputted value outside range 2 < X < 19"

  def test_ok_smallest_3(self):
    x = 3
    result = myfunc(x)
    total_event = result['total_event']
    event_prob = result['event_prob']
    
    expected_total_event = 1
    expected_event_prob = float(format(expected_total_event/TOTAL_EVENT, ".3f"))

    self.assertEqual(total_event, expected_total_event)
    self.assertEqual(event_prob, expected_event_prob)
  
  def test_ok_max_18(self):
    x = 18
    result = myfunc(x)
    total_event = result['total_event']
    event_prob = result['event_prob']
    
    expected_total_event = 1
    expected_event_prob = float(format(expected_total_event/TOTAL_EVENT, ".3f"))


    self.assertEqual(total_event, expected_total_event)
    self.assertEqual(event_prob, expected_event_prob)
  
  def test_ok_15(self):
    x = 15
    result = myfunc(x)
    total_event = result['total_event']
    event_prob = result['event_prob']
    
    expected_total_event = 10
    expected_event_prob = float(format(expected_total_event/TOTAL_EVENT, ".3f"))

    self.assertEqual(total_event, expected_total_event)
    self.assertEqual(event_prob, expected_event_prob)
  
  def test_zero_sum(self):
    x = 0
    result = myfunc(x)
    self.assertEqual(result, err_msg_outside_range)
      
  def test_negative_sum(self):
    x = -3
    result = myfunc(x)
    self.assertEqual(result, err_msg_outside_range)

  def test_more_than_max(self):
    x = 20
    result = myfunc(x)
    self.assertEqual(result, err_msg_outside_range)

if __name__ == '__main__':
  unittest.main()
  


