year_ = int(input("year: "))
month_ = int(input("month: "))
day_ = int(input("day: "))

month_arr_ = [0,31,59,90,120,151,181,212,243,273,304,334]
if 0 < month_ <= 12:
    sum = month_arr_[month_-1]
else:
    print("data error")

sum += day_
leap = 0
if year_%400==0 or year_%4==0 and year_%100!=0:
    leap = 1
if leap==1 and month_>2:
    sum += 1
print("totally days: {}".format(sum))