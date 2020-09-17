# Author: Boyuan Lai bjl5716@psu.edu
# Collaborator: Alex Podlucky app5775@psu.edu
# Collaborator: Ilysa Sanchez-Perez ims5280@psu.edu
# Collaborator: Hetvi Devani hdd5060@psu.edu
# Section: 12
# Breakout: 10
def sum_n(n):
  if n == 0:
    return n
  else:
    return n+sum_n(n-1)

def print_n(s, n):
  if n == 0:
    return
  else:
    print(s)
    print_n(s,n-1)
    return

def run():
  num = int(input("Enter an int: "))
  print (f"sum is {sum_n(num)}.")
  letter = input("Enter a string: ")
  print_n(letter, num)
  
if __name__ == "__main__":
  run()