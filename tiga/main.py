"""_summary_
Given Fib sequence which start from X and Y where X and Y > 0. 
Find the sum of even number, and sum of odd number in the sequence from N number of sequence where 2 < N < 1000000 


-- Example 
X = 2,  Y= 3, N = 3
2, 3, 5
sum of even = 2
sum of odd = 8
"""

"""

pseudocode

1. Accept (X, Y, N) > 0 
2. Iterate in range N 
"""

def sum_even_and_odd_from_fib_number(X : int, Y: int, N: int):
  err_msg_must_positive_number = f"value inputted should be positive : X & Y > 0"
  err_msg_must_in_range = f"value N should be in range : 2 < N < 1000000"

  if X <= 0 or Y <= 0 :
    return err_msg_must_positive_number
  
  if N < 2 :
    return err_msg_must_in_range

  print (f"x = {X} | y = {Y} | n = {N} ")
  fibs = {}
  fibs[0] = X
  fibs[1] = Y
    
  idx = 0
  while len(fibs) < N:
    fibs[idx+2] = fibs[idx] + fibs[idx+1]
    # print(fibs)
    idx += 1

  print(f"fibs = {fibs}")
  s_even, s_odd = sum_even_and_odd_number(fibs)   
  print(f"sum of even = {s_even}")
  print(f"sum of odd = {s_odd}")
  print(f"len = {len(fibs)}")

  return s_even, s_odd, len(fibs)

def sum_even_and_odd_number(fibs):
  ttl = ev = odd = 0   
  for idx in fibs:
    fib = fibs[idx]
    ttl += fib    
    if fib % 2 == 0:
      ev += fib
    else:
      odd += fib
  
  print(f'sum total = {ttl}')
  return ev, odd

# main(2,3,7)