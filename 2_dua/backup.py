
class Rice:
  def __init__(self, price = None):
    self.name : str = "Rice"
    self.gr_cals : float = 28 
    self.gr_carbs : float = self.gr_cals / 4
    self.price = price
  
  def price_per_gram_carbs(self):
    self.price_per_gram_carbs = (self.price / self.gr_carbs)
  
  def desc(self):
    msg = f"name: {self.name} | price = {self.price}  "
    return msg

class Corn:
  def __init__(self, price = None):
    self.name :str = "Corn"
    self.gr_cals :float = 21
    self.gr_carbs :float = self.gr_cals / 4
    self.price :float = price
  
  def get_price_per_gram_carbs(self):
    return format((self.price / self.gr_carbs),".3f")

  def desc(self):
    per_gr = self.get_price_per_gram_carbs()
    msg = f"name: {self.name} | price = ${self.price} | gr carbs = {self.gr_carbs} | price per gr = {per_gr} "
    return msg

class Potato:
  def __init__(self, price = None):
    self.gr_cals : float = 17
    self.gr_carbs : float = self.gr_cals / 4
    self.price = price

rice = Rice()
corn = Corn()
potato = Potato()

print(f"rice, cals = {rice.gr_cals} | carbs = {rice.gr_carbs} ")
print(f"corn, cals = {corn.gr_cals} | carbs = {corn.gr_carbs} ")
print(f"potato, cals = {potato.gr_cals} | carbs = {potato.gr_carbs} ")
