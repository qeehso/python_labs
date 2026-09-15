minutes = int(input('Минуты:'))

hours = (minutes // 60) % 24
external_minutes = minutes % 60 

print(f'{hours}:{external_minutes:02d}')