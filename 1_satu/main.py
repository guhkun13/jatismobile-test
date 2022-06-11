import math
import time

MIN_CAP = 0
MAX_CAP = 30

MIN_LITTER = 100
MAX_LITTER = 1_000_000_000

def is_allowed(*args):
  allowed_range = is_allowed_range(*args)
  if not allowed_range:
    return False
  
  return is_prime_number(*args)

def is_allowed_range(*args):  
  is_allowed = True
  for arg in args:
    if arg < 0 or arg > 30:
      is_allowed = False    

  return is_allowed

def is_prime_number(*args):
  for arg in args:
    for i in range (2, int(math.sqrt(arg))+1):
        if (arg % i ) == 0:
          return False

  return True      

def solution(b1: int, b2: int, b3: int, x: int):
  st_time = time.perf_counter()
  err_msg_positive_and_prime_number   = f"value inputted should be positive and prime number : {MIN_CAP} < x < {MAX_CAP}"
  err_msg_litter_milk_outside_range   = f"value milk litter should be integer range : {MIN_LITTER} < x < {MAX_LITTER}"

  if x < MIN_LITTER or x > MAX_LITTER:
    return err_msg_litter_milk_outside_range
  
  if not isinstance(x, int):
    return err_msg_litter_milk_outside_range

  if not is_allowed(b1, b2, b3):
    return err_msg_positive_and_prime_number
  
  bottles = [
    {"name": "b1", "value":b1, "count" : 0},
    {"name": "b2", "value":b2, "count" : 0},
    {"name": "b3", "value":b3, "count" : 0},
  ]
  sorted_bottles = sorted(bottles, key=lambda x:x['value'], reverse=True)
  # print(sorted_bottles)

  ttl_item = 0
  diff_ltr = x
  items_needed = []
  
  idx = 0
  while diff_ltr > 0:
    thedict = sorted_bottles[idx]
    ttl_item, diff_ltr, items_needed = do_magic(thedict, ttl_item,  diff_ltr, items_needed)
    idx += 1
  
  exc_time = time.perf_counter() - st_time
  print (f"exec time = {exc_time}")
  # print(f"items_needed = {items_needed}")

  return ttl_item

def do_magic(it:dict, ttl_item,  diff_ltr, items_needed:list):
  n_item = diff_ltr // it.get('value')
  if not n_item:
      n_item = 1
  ttl_item = ttl_item + n_item
  ttl_ltr = n_item * it.get('value')

  diff_ltr = diff_ltr - ttl_ltr
  it.update({"count": ttl_item})
  items_needed.append(it)

  return ttl_item, diff_ltr, items_needed

print(solution(5,11,7,100))