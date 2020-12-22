print("------ComNum-----")
M = input("choose mode(1.Re;2.Im):")
Z = input("What's your number:")
if M == '1':
    print("Re(Z)={:.2f}".format(complex(Z).real))
elif M == '2':
    print("Im(Z)={:.2f}".format(complex(Z).imag))
else:
    print("!WRONG MODE!")
