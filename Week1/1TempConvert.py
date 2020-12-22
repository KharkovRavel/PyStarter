# TempCovert.py
print("----------TempConvert----------\nConvert Temperature data between Celsius, Fahrenheit and Kelvin!\n")
TempStr = input("Please input the temperature in the format like \"125F\":")
if TempStr[-1] in ['f', 'F']:
    C = (eval(TempStr[0:-1])-32)/1.8
    K = C + 273.15
    print("The temperature converted is {:.2f}C,{:.2f}K".format(C, K))

elif TempStr[-1] in ['c', 'C']:
    F = 1.8*eval(TempStr[0:-1])+32
    K = eval(TempStr[0:-1]) + 273.15
    print("The temperature converted is {:.2f}F,{:.2f}K".format(F, K))

elif TempStr[-1] in ['k', 'K']:
    C = eval(TempStr[0:-1])-273.15
    F = 1.8*C+32
    print("The temperature converted is {:.2f}F,{:.2f}C".format(F, C))
else:
    print("!Wrong Format!")
