import json
from textwrap import indent
"""_summary_
From 3 6-side-dice, find the probability to find the sum of three dices number is equal to X where 2 < X < 19. 

Facts:
1. rolling n dices, there are 6^n outcomes / possibilities
    3 dices = 6^3 = 216 outcomes 
2. Greatest number on dice is 6, smallest one is 1. 
3. when N dice are rolled, smallest possible sum is N and max possible is 6N
4. using permutation to count possibility each sum needed

source : https://www.thoughtco.com/probabilities-for-rolling-three-dice-3126558

solutions:
1. create dict for each possible sum outcomes
2. there should be 16 possible sum 3 - 18
"""

# there 
DICES = 3
TOTAL_EVENT = 6**DICES

idx = 0 
ordered_sum_probs = [1,3,6,10,15,21,25,27,27,25,21,15,10,6,3,1]
# print("total sum probs : ",len(ordered_sum_probs))

dict_prob = {}
# list_prob = []
for i in range (3,19):
  event = ordered_sum_probs[idx]
  event_prob = float(format( event / TOTAL_EVENT, ".3f"))
  # print (f"i = {i} | idx = {idx} | item = {ordered_sum_probs[idx]}")
  # print (f"event = {event} | total event = {TOTAL_EVENT} | event_prob = {event_prob}")

  items = {
    'sum' : i, 
    'total_event':event,
    'event_prob': event_prob, 
    'percentile': str(format(event_prob * 100, ".1f")) + "%"
  }
  idx += 1
  dict_prob.update({i:items})

CONST_DICT_PROB = dict_prob
json_dict = json.dumps(CONST_DICT_PROB, indent=2)
print(json_dict)

def found_probability_for_sum(sumx:int):
  print (f"find prob for sum {sumx}")

  err_msg_outside_range = "your inputted value outside range 2 < X < 19"
  if sumx < 3 or sumx > 18:
    print(f"Error: {err_msg_outside_range}")
    return err_msg_outside_range
  
  
  result = CONST_DICT_PROB.get(sumx)
  print(f"result = {result}")
  
  return result
