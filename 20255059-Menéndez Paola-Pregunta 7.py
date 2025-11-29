# EJERCICIO 8 - VALIDACIÓN DE DUI
#caso1
DUI = input()
cond1 = len(DUI)==10
cond2 = DUI[8]=='-'
cond3 = DUI[-1]==int
print(len(DUI)==10 and DUI[8]=='-')
#caso2
DUI = input()
cond1 = len(DUI)==10
cond2 = DUI[8]=='-'
cond3 = DUI[-1].isdigit()
print(cond1 and cond2 and cond3)
#caso3
DUI = input()
cond1 = len(DUI)==10
cond2 = DUI[8]=='-'
cond3 = DUI[-1].isdigit()
print(cond1 and cond2 and cond3)
