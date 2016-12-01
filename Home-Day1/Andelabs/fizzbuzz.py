# Program that checks whether a number is divisible by 3 or 5, 3 and 5 at the same time and returns the input if neither
# Author: Evans Wanjau
def fizz_buzz(n):
  # Statement that checks whether its divisible by both 3 and 5
  if n % 3 == 0 and n % 5 == 0:
    return 'FizzBuzz'
  # Statement that checks whether its divisible by 5
  elif n % 5 == 0:
    return 'Buzz'
  # Statement that checks whether its divisible by both 3
  elif n % 3 == 0:
    return 'Fizz'
  # Statement that returns the input if not divisible by either
  else:
    return n
