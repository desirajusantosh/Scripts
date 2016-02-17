import re
#dir(re) to list all the 
#re.search() - returns leftmost match of the pattern in a line
  #match = re.search('pattern', 'text')
  
#.  match any character
#\w match word character
#\d match digit
#\s match whitespace
#\S match non-whitespace character
#\ Escape character
#+ Match one or more thing(s) it follows.
#* Match zero or more thing(s) it follows.
#[] Character class to match a character.
#() Grouping characters  
  
  
match = re.search(r'(\w+).*(time.*)', 'Good times ahead')
match.group()
if match:
  print match.group()
  print match.group(1)
  print match.group(2)
else:
  print 'match not found'
  
  
  
