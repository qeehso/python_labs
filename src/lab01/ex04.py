minutes = int(input('Введите целое количество минут:'))

hours = minutes // 60 
external_minutes = minutes % 60 

print(f'{hours}:{external_minutes:02d}')