"""
  _test summary_ : 
  An adult man needs 400 grams of carbohydrate each day. Following is some of food for 100 grams: 

  Rice      28 grams Cal
  Corn      21 grams Cal
  Potato    17 Grams Cal

  For each day, the price of each food per 100 grams is changing. Thus make a program to solve such that the cost of food is keep minimum (lowest) while still maintaining ~400 grams carbohydrate needed for body 
"""

"""
Info needed:
1. 1 gr carbs = 4 gr cal , so 400 gr carbs each day = 4x400 = 1600 Cal each day needed. 
  1 gr CARBS = 4 gr CAL. 

2. the gram Cal each product have is CONSTANT as described below per 100 gram product. 
3. the price of product per 100 grams is changing each day. 

4. the program will accept 3 input parameter (float) as kwargs 
  {product_name : price_per_100grams} 

Example : 
-- the price for 100 grams rice, corn and potatoes per 100 grams are following : (2.0,1.5,3.8) in dollar. 
  how much cost the adult man needed to have 400 grams carbs ? 
"""

"""
psedocode:
1. Find cheapest product per gram = price / product.carbs as ITEM
2. Count how many ITEM needed = 400 gr / ITEM.carbs as N ITEM (math.floor)
3. Count TTL_PRICE = N ITEM x ITEM.price and TTL_CARBS = N ITEM x ITEM.carbs
3.a check if TTL_CARBS >= 400, if not then 
  1. get second cheapest product! repeat process 1 & 2 , added to existing TTL_CARBS and TTL_PRICE
3.b iF TTL_CARBS >= 400 , finish the program. return TTL_PRICE
"""

import math

TOTAL_CARBS_NEEDED = 400
RICE_CALS = 28
CORN_CALS = 21
POTATO_CALS = 17

def find_minimum_cost_food(**kwargs):
  # define error message
  err_msg_must_be_positive_number = "Price must be positive number below a hundred: 0 < x < 100"
  
  for k, v in kwargs.items():
    print(f"{k} = ${v} per 100 gr")

    if v <= 0 or v > 100:
      err = err_msg_must_be_positive_number
      print (f"Error on price {k}: {err}")
      return err
  
  rice_price = kwargs.get('rice')
  corn_price = kwargs.get('corn')
  potato_price = kwargs.get('potato')

  corn_prop = {
    'name' : 'corn',
    'price' : corn_price,
    'gr_cals' : CORN_CALS,
    'gr_carbs': CORN_CALS/4,  
  }

  rice_prop = {
    'name' : 'rice',
    'price' : rice_price,
    'gr_cals' : RICE_CALS,
    'gr_carbs': RICE_CALS/4
  }

  potato_prop = {
    'name' : 'potato',
    'price' : potato_price,
    'gr_cals' : POTATO_CALS,
    'gr_carbs': POTATO_CALS/4
  }
  
  rice_prop['price_per_gr'] = float(format(rice_price / rice_prop['gr_carbs'], ".3f"))
  corn_prop['price_per_gr'] = float(format(corn_price / corn_prop['gr_carbs'], ".3f"))
  potato_prop['price_per_gr'] = float(format(potato_price / potato_prop['gr_carbs'], ".3f"))
  props = rice_prop, corn_prop, potato_prop

  # print(props)
  print(rice_prop)
  print(corn_prop)
  print(potato_prop)

  # 1. Find cheapest product
  prices = [rice_prop['price_per_gr'], corn_prop['price_per_gr'], potato_prop['price_per_gr']]
  # print(prices)
  prices.sort()
  print(prices)

  items_needed = []
  total_price = total_carbs = total_item = 0
  carbs_needed = TOTAL_CARBS_NEEDED
  idx = 0
  while total_carbs < TOTAL_CARBS_NEEDED:
    carbs_needed = carbs_needed - total_carbs
    print(f"idx = {idx} | carbs needed ] {carbs_needed}")
    total_price, total_carbs, total_item = get_total_price_and_carbs_by_price(total_price, total_carbs, total_item, prices[idx], props, carbs_needed, items_needed)
    print(f"total price = ${total_price}")
    print(f"total carbs = {total_carbs}")
    idx += 1
    print ("==========================")
  
  print ("--- FINAL RESULT --- ")
  print (f"total price : ${total_price} with carbs = {total_carbs} | total_item needed = {total_item} ")
  print ("item needed")
  for item in items_needed:
    print(item)

def get_total_price_and_carbs_by_price(total_price, total_carbs, total_item, price, props, carbs_needed, items_needed):
  # 1.a GET prop based on price_per_gr
  cheapest_prop = None
  for prop in props:
    if prop['price_per_gr'] == price:
      cheapest_prop = prop

  print(f"cheapest_prop = {cheapest_prop}")
  
  # 2. Count ITEM needed as N from total CARBS needed / carbs  
  n_item = math.floor(carbs_needed / cheapest_prop['gr_carbs'])
  if n_item <= 0:
    n_item = 1
  print(f"n item = {n_item}")
  total_item = total_item + n_item
  # 3. count total_price
  total_price += float(format(n_item * cheapest_prop['price'], ".3f"))
  total_carbs += math.floor(n_item * cheapest_prop['gr_carbs'])
  
  items_needed.append({'count': n_item, 'prop': cheapest_prop})

  return total_price, total_carbs, total_item

# Call main function
# find_minimum_cost_food(rice = 2.0, corn = 1.4, potato = 1.8)

find_minimum_cost_food(rice = -2.0, corn = 1.4, potato = 1.8)
find_minimum_cost_food(rice = 2.0, corn = 0.0, potato = 1.8)
find_minimum_cost_food(rice = 2.0, corn = 10.0, potato = 100.8)
