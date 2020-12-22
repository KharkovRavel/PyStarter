# Automatically-refreshed progress bar ver.MultipleLines
import time
scale = 10
print("----------START----------")
for i in range(scale+1):
    a = '*' * i  # a is a string which repeats for i times
    b = '.' * (scale-i)
    c = (i/scale) * 100
    print("{:^3.0f}%[{}->{}]".format(c, a, b))
    time.sleep(0.1)
print("----------END----------")
