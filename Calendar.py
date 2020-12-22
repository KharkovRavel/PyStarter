# PyCalendar
import calendar
# calendar Phase 1
# c = calendar.TextCalendar(calendar.MONDAY)
# c.prmonth(2019, 7)  # Show the calendar of July 2019
# c.prmonth(2020, 12)
# calendar Phase 2
import pprint

cal = calendar.Calendar(calendar.SUNDAY)

cal_data = cal.yeardays2calendar(2019,7)
# yeardays2calendar:生成月份行列表，日期编号1-31，工作日编号0-6，超出月份的天数为0
print('len(cal_data)        :', len(cal_data))

top_months = cal_data[0]
print('len(top_months)      :', len(top_months))

first_month = top_months[0]
print('len(first_month)     :', len(first_month))

print('first_month:')
pprint.pprint(first_month, width=65)

# 运行结果：（日期，星期），每行为一周

