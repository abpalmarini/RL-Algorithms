# Methods for printing out the gridworld values and policies.

def print_grid_values(grid_values):
  rows, columns = grid_values.shape
  for row in range(rows):
    print_row_border(columns) 
    print_row_values(grid_values[row])
  print_row_border(columns)
  print('')

def print_grid_policy(grid_policy):
  rows, columns = grid_policy.shape
  for row in range(rows):
    print_row_border(columns) 
    print_row_policy(grid_policy[row])
  print_row_border(columns)
  print('')

def print_row_border(n):
  print('|======='*(n-1), end='')
  print('|=======|')

def print_row_values(row):
  for value in row:
    #if value == 0:
    #  print('|///////', end='')
    if value < 0 and abs(value) >= 10:
      print('| {:.1f} '.format(value), end='')
    elif value < 0:
      print('| {:.1f}  '.format(value), end='')
    else:
      print('|  {:.1f}  '.format(value), end='')
  print('|')

arrows = {0:'←', 1:'↑', 2:'→', 3:'↓'}

def print_row_policy(row):
  for policy in row:
    if policy == None:
      print('|///////', end='')
      continue
    actions = [c for c, v in enumerate(policy) if v > 0]
    n = len(actions)
    print('|', end='')
    if n % 2 == 0:
      print(' '*((7-n-1)//2), end='') # 7 is number of spaces in a grid
      for a in actions:
        print(arrows[a], end='')
      print(' '*((7-n+1)//2), end='')
    else:
      print(' '*((7-n)//2), end='')
      for a in actions:
        print(arrows[a], end='')
      print(' '*((7-n)//2), end='')
  print('|')
      
