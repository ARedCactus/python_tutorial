str_1 = "12"
num = 0
for x in str_1:
    num = 8 * num + ord(x) - ord('0')
print(num)