print(" ****Electricity Bill****"   )
name=input("Enter biller Name->")
unit=int(input("Enter the unit of elctrcity->"))
if unit<=50:
    total = unit* 0.50
    extra = total * 20 / 100
    tt=total+extra
    print(" Elctricity bil is  RS->", total,"\n Extra charge RS->", extra,"\n   total bill of Electrecity->",tt)
elif unit<=100:
    total = unit * 0.75
    extra = total * 20 / 100
    tt = total + extra
    print(" Elctricity bil is  RS->", total, "\n    Extra charge->", extra,"\n  total bill of Electrecity->",tt)
elif unit<=150:
    total = unit * 1.20
    extra = total * 20 / 100
    tt = total + extra
    print(" Elctricity bil is  RS->", total, "\n    Extra charge->", extra,"\n  total bill of Electrecity->",tt)
else:

        total = unit * 1.50
        extra = total * 20 / 100
        tt = total + extra
        print(" Elctricity bil is  RS->", total, "\n    Extra charge->", extra, "\n  total bill of Electrecity->", tt)
list=[name,"-",str(unit),"-",str(tt),"\n"]
newpath="D:\py_autoGUI\dd.csv"
new=open(newpath,"a")
new.writelines(list)
