""""
  A Company have 3 different capacity of milk bottle, which the milk bottle capacity is prime number between 0 to 30 litters (0 < Bottle x < 30).

  How many bottles from each different capacity does the company need to contain X litters of milk (100 < X < 1000000 ) such that the total number of bottles needed is the fewest ? 

  Ex:
   Bottle 1 = 5 litter
   Bottle 2 = 7 litter
   Bottle 3 = 11 Litter
   X = 100 
   Ans :
   Bottle 3 = 9, Bottle 1 = 1 bottle, Bottle 2 = 0 bottle, total = 10 bottles
   or    
   Bottle 3 = 9, Bottle 1 = 0 bottle, Bottle 2 = 1 bottle, total = 10 bottles
"""

import math

MIN_CAP = 0
MAX_CAP = 30

MIN_LITTER = 100
MAX_LITTER = 1000000

def is_allowed(*args):
  ''' Accept n integers, check if it positive integer 0 < x < 30 and prime number '''
  allowed_range = is_allowed_range(*args)
  if not allowed_range:
    return False
  
  return is_prime_number(*args)

def is_allowed_range(*args):  
  ''' Accept n integers, check if it positive integer 0 < x < 30 '''
  is_allowed = True
  for arg in args:
    print(arg)
    if arg < 0 or arg > 30:
      is_allowed = False
    
  return is_allowed

def is_prime_number(*args):
  ''' Accept n integers, check if it is prime number '''
  for arg in args:
    for i in range (2, int(math.sqrt(arg))+1):
        if (arg % i ) == 0:
          return False

  return True      

def find_fewest_bottle(b1: int, b2: int, b3: int, x: int):
  """
  Find newest bottle needed using 3 types of bottle
  b1,b2,b3 or bx must be 0 < bx < 30 and x must be 100 < X 1000000 
  Args:
      b1 (int): capacity bottle 1 in litter
      b2 (int): capacity bottle 1 in litter
      b3 (int): capacity bottle 1 in litter
      x  (int): litter of milk that needed to be contained

  Returns:
      int: total bottle needed to contain X litter
  """

  print(f" Bottle 1: {b1} litter | Bottle 2: {b2} litter | Bottle 3: {b3} litter | X: {x} litter")
  err_msg_positive_and_prime_number   = f"value inputted should be positive and prime number : {MIN_CAP} < x < {MAX_CAP}"
  err_msg_litter_milk_outside_range   = f"value milk litter should be : {MIN_LITTER} < x < {MAX_LITTER}"

  if x < 100 or x > 1000000:
    return err_msg_litter_milk_outside_range

  cb1 = cb2 = cb3 = 0
  if not is_allowed(b1, b2, b3):
    return err_msg_positive_and_prime_number
  
  count_bottles = (
    {
      b1 : 0,
      b2 : 0,
      b3 : 0
    }
  )

  print(f"count_bottles = {count_bottles}")
  bottles = [b1, b2, b3]
  print(bottles)

  bottles.sort(reverse=True)
  print(bottles)

  while x > 0:
    if (x - bottles[0]) > 0:
      x -= bottles[0]
      count_bottles[bottles[0]] += 1      
    elif (x - bottles[1]) > 0:
      x -= bottles[1]      
      count_bottles[bottles[1]] += 1
    else:
      x -= bottles[2]
      count_bottles[bottles[2]] += 1
  
  cb1, cb2, cb3 = count_bottles[b1], count_bottles[b2], count_bottles[b3]
  ttl = cb1 + cb2 + cb3
  print(f"Count Bottle needed | Bottle 1-{b1}L: {cb1} | Bottle 2-{b2}L: {cb2} | Bottle 3-{b3}L: {cb3} | - Total bottle: {ttl} btl ")
  return ttl
  
print(find_fewest_bottle(5,29,7,100))