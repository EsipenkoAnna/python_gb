my_list = []
for value in range (1, 1000, 2):
    my_list.append(value**3)
print(my_list)
main_summ = 0
for num in range(len(my_list)):
    sum = 0
    val = my_list[num]
    print (val)

    while(val!=0):
        sum = sum + val%10
        val=val//10
        print(sum)

   ## if sum%7==0:
   ##     result =+main_summ
  ##  print(main_summ)

