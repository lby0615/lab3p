# Author: Boyuan Lai bjl5716@psu.edu
# Collaborator:
# Collaborator:
# Collaborator:
# Section: 1
# Breakout: 12
def sum_n(n):
  if n <= 1:
    return 1
  else:
    return n+sum_n(n-1)

def print_n(s, n):
  return s*n

def run():
  num = int(input("Enter an int: "))
  print (f"sum is: {sum_n(num)}")
  letter = input("Enter a string:")
  print (print_n(letter, num))
  

if __name__ == "__main__":
  run()