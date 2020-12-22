# ver.SingleLine
import time
scale = 100
print("START EXECUTING".center(scale, "-"))
start = time.perf_counter()
for i in range(scale + 1):
    a = '*' * i  # a is a string which repeats for i times
    b = '.' * (scale - i)
    c = (i / scale) * 100
    dur = time.perf_counter()-start
    print("\r{:.^3.1f}%[{}->{}]){:.2f}s".format(c, a, b, dur), end='')  # ^:表示居中;\\\
    # end='':使此句结束后不换行
    time.sleep(0.1)
print("\n"+"END".center(scale, '-'))
