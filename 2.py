days = 0
count = 1

month_1 = 30
month_2 = 31

for i in range(1900,2000):
    if (i % 4 ==0 and not i % 100 !=0) or (i % 400 == 0):
        moth = 29
    else:
        moth = 28
        for month in range(1,13):
            if month == 2:
                days += moth
            elif (month == 1) or (month == 3) or (month == 5) or (month == 7) or (month == 8) or (month == 10) or (month == 12):
                days += month_2
            else:
                days += month_1
                
            print (days)
            if days % 7 == 0 or i > 1900:
                count +=1
print(count)
                
