def Percents_choise(numb: int) -> str:
 if numb == 1:
    choise = f'{numb} Процент'
 elif numb == 2:
    choise = f'{numb} Процентов'
 else:
    choise = f'{numb} Процента'
    return choise

 for numb in range (1, 6):
    print(Percents_choise(numb))
