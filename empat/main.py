"""_summary_
Given random string, count the occurence of each character in the string 
and sort them according to UTF-8
"""
def count_and_sort(randstring:str):
  print (f"input string = {randstring}")

  strlist = []
  strcount = {}
  for s in randstring:
    if s not in strcount:
      strlist.append(s)      
      strcount.update({s:1})
    else:
      incr = strcount.get(s) + 1
      strcount.update({s:incr})
  
  strlist.sort()
  print(strcount)
  print(strlist)

  return strcount, strlist

count_and_sort("nama saya adalah teguh atma")