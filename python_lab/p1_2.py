unit=int(input("enter the units:"))
if unit<=200:
    bill=100
elif unit>=200 and unit<=400:
    extra=unit-200
    bill=100+(extra*0.65)
elif unit>=401 and unit <=600:
    extra=unit-400
    bill=100+130+(extra*0.8)
elif unit>600:
    extra=unit-600
    bill=100+130+160+(extra*1)

if bill>=400:
    bill=bill+bill*0.15
print("Cost for",unit,"unit is:",bill)