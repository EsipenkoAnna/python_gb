my_list = []
new_my_list =[]

for value in range (1, 1000, 2):
    my_list.append(value**3)
print(my_list)

def sum_numbers(numb):
    sum_n = 0
    while numb != 0:
        sum_n += numb%10
        numb=numb//10
        return sum_n

def sum_list (dataset:list)->int:
    sum1 = 0
    list2 = []
    for i in dataset:
        a=sum_numbers(i)
        if a%7==0:
            list2.append(i)
    for i in list2:
        sum1 += i
    return sum1

for value in my_list:
    new_value=value+17
    new_my_list.append(new_value)


result = sum_list (my_list)
print(result)
result1 = sum_list (new_my_list)
print(result1)