def dayUP(df):
    dayup = 1
    for i in range(365):
        if i % 7 in [6, 0]:
            dayup *= (1-df)
        else:
            dayup *= (1+df)
    return dayup

dayfactor = 0.01
dayup = dayUP(dayfactor)
print("{:.2f}".format(dayup))
