def print_grid(grid_array):
  n = grid_array.shape[0]
  for row in range(n):
    print_row_border(n) 
    print_row_numbers(grid_array[row])
  print_row_border(n)

def print_row_border(n):
  print('|======'*(n-1), end='')
  print('|======|')

def print_row_numbers(row):
  for value in row:
    if value == 0:
      print('|//////'.format(value), end='')
    elif value < 0 and abs(value) >= 10:
      print('|{:.1f} '.format(value), end='')
    elif value < 0:
      print('|{:.1f}  '.format(value), end='')
    else:
      print('|{:.1f}    '.format(value), end='')
  print('|')
