a = float(input('a:').replace(',', '.'))  # change ',' to '.'  
b = float(input('b:').replace(',', '.'))  # change ',' to '.'
sum = a + b
avg = sum / 2
print(f'sum={sum:.2f}, avg={avg:.2f}') # we take only 2 decimal places

