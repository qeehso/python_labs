strange_text = input("Введите шифр:")
orig = ''
first = 0  #  for defining the step
second = 0  

for i in range(len(strange_text)):  # searching for the first uppercase letter
    if strange_text[i].isupper():
        orig += strange_text[i]
        first = i
    if strange_text[i].isdigit():
        orig += strange_text[i+1]
        second = i + 1
        break

step = second - first # defining the step

for j in range(second+step, len(strange_text), step):
    orig += strange_text[j]

print(orig)  # output the original text
