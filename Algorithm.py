print("Please enter the day, month and year of the date to calculate as numbers")

q = int(input("day: "))
m = input("month: ")
m = int(m)
year = int(input("year: "))

k = year%100
j = year//100

if(m<3):
    m = m+12
    k = k - 1

h=(q+(13*(m+1)//5)+k+(k//4)+(j//4)-(2*j))%7
#h=day of week (0=saturday, 1=sunday etc)
#q=day of month
#m=month (3=march, 4=april, 5=may...14=feb)
#k=(year%100)
#j=(year/100)
print(h)