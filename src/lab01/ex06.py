N = int(input('Всего строк:'))
in_ = {}  # set of the strings
ochno = 0

for i in range(1,N+1):
    in_[i] = input(f'Введите {i} строку:')
    ochno += in_[i].split()[-1] == 'True'  # ochnoe quantity 
print(ochno, N-ochno)  

