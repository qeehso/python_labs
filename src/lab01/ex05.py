fio = input('Введите ФИО:')
words = fio.split()
initials = ''

for word in words:
    first_letter = word[0].upper()
    initials += first_letter 
print(initials + '.')  # initials

len_without_odd_spaces = len(fio.replace(' ', ''))  # len without any spaces (слитно всё)
len_with_normal_spaces = len_without_odd_spaces + len(words) - 1  # normal quantity of spaces = quantity of words - 1 
print(len_with_normal_spaces)  # len with normal quantity of spaces