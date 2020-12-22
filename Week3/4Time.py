import time as t
tf = t.time()
tr = t.ctime()
tpc = t.gmtime()

print("time in float:{:.2f}".format(tf))
print("time readable:", tr)
print("time for pc:", tpc)

tformat = t.strftime("%Y-%m-%d %H:%M:%S", tpc)

