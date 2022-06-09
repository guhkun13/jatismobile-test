"""_summary_
Given random string, count the occurence of each character in the string 
and sort them according to UTF-8
"""
def count_and_sort(randstring:str):
  print (f"input string = {randstring}")

  strlist = []
  strcount = {}  
  for s in randstring:
    strlist.append(s)      
    if s not in strcount:      
      strcount.update({s:1})
    else:
      incr = strcount.get(s) + 1
      strcount.update({s:incr})
  
  strlist.sort()

  onestr = "".join(strlist)
  print(f"onestr={onestr}")
  print(f"strcount={strcount}")

  return onestr, strcount


count_and_sort("abcxx ")