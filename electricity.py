unit=int(input("inter the unit of elctrcity"))
if unit<=50:
    total = unit* 0.50
    extra = total * 20 / 100
    tt=total+extra
    print("elctricity bil is  RS", total,"\n extra charge", extra,"\n total bill of electrecity",tt)
elif unit<=100:
    total = unit * 0.75
    extra = total * 20 / 100
    tt = total + extra
    print("elctricity bil is  RS", total, "\n extra charge", extra,"\n total bill of electrecity",tt)
elif unit<=150:
    total = unit * 1.20
    extra = total * 20 / 100
    tt = total + extra
    print("elctricity bil is  RS", total, "\n extra charge", extra,"\n total bill of electrecity",tt)
else:

    total = unit * 1.50
    extra = total * 20 / 100
    tt = total + extra
    print("elctricity bil is  RS", total, "\n extra charge", extra,"\n total bill of electrecity",tt)
