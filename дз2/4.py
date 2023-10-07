x = input()
a = x.count(')')
b = x.count('(')
if a == b:
    print("Всё в порядке")
elif a < b:
    print("Не хватает закрывающей скобки")
else:
    print("Не хватает открывающей скобки")
