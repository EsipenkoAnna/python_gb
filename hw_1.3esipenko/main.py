def Percents_choise(numb: int):
 if numb == 1:
    choise = f'{numb} Процент'
 elif numb == 2:
    choise = f'{numb} Процентов'
 else:
    choise = f'{numb} Процента'
    return choise

 for numb in range (1, 6):
    a = Percents_choise(numb)
    print(a)
print (124)
