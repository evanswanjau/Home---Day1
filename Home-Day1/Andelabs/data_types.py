def data_type(x):
  x = "hello"
  if x.isalpha:
    n = len(x)
    print(n)
    
  if isinstance(x, None):
    return 'no value'
  
  if isinstance(x, bool):
    return x
    
  if isinstance(x, int):
    if x > 100:
      return 'more than 100'
    elif x < 100:
      return 'less than 100'
    else:
      return 'equal to 100'
  
  if isinstance(x, list):
    return x[2]