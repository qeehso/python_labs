price = float(input("Введите цену товара:"))

discount = float(input("Введите скидку в процентах:"))
if discount < 0 or discount > 100:  # logical )))
    print("Ошибка: скидка должна быть в диапазоне от 0 до 100 процентов.")
    exit()

vat = float(input('Введите НДС в процентах::'))
if vat < 0 or vat > 100:  # also logical
    print("Ошибка: НДС должен быть в диапазоне от 0 до 100 процентов.")
    exit()

base = price * (1 - discount/100)
vat_amount = base * (vat/100)
total = base + vat_amount 

print(f'База после скидки: {base:.2f}')  # we take only 2 decimal places
print(f'НДС: {vat_amount:.2f}')
print(f'Итого к оплате: {total:.2f}')