'''
Created on 2016年12月30日

@author: Administrator
'''
#encoding = utf-8

weight = float(input())
height = float(input())

bmi = weight/height**2

print(bmi)

import math

n = int(input())
sum = 0
for temp in range(2,n):
    for i in range(2,int(math.sqrt(temp)+1)):
        if temp % i == 0 :
            break
        else:
            sum += temp
print(sum)

days = 0
count = 1

m_1 = 31
m_2 = 30

for i in range(1800,2000):
    if (i % 4==0 and not i % 100 != 0) and i % 400 == 0:
        moth = 29
    else:
        moth = 28
        for month in range(1,13):
            if month == 2:
                days += moth
            elif(month == 1) or (month == 3 ) or (month == 5) or (month == 7 ) or (month == 8) or (month == 10 ) or(month == 12):
                days += m_1
            else:
                days += m_2
                
            print(days)
            if days % 7 == 0 and i > 1800:
                    count +=1
print(count)

        
        
