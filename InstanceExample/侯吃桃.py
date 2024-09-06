def func(now_num, days):
    for x in range(days-1, 0, -1):
        now_num = (now_num+1) * 2
    return now_num

num = func(1, 10)
print(num)