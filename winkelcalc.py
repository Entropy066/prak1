#Eingaben: x1,x2
#winkel ausrechnen

#h1 ist parallel zur x achse, y nicht.
import math as mt

x1 = float(input("Enter X1: "))
y1 = float(input("Enter Y1: "))


y2 = float(input("Enter Y2: "))
while y2 < y1:
    y2 = float(input(f"ERROR!, Y2 needs to be bigger than Y1({y1}), input valid Y2 now: "))
else: 
    pass

x2 = float(input("Enter X2: "))
while x2 < x1:
    x2 = float(input(f"ERROR!, X2 needs to be bigger than X1({x1}), input valid X2 now: "))
else:
    pass

B = (x1, y1)
C = (x1,y2)
A = (x2, y2)

a = (C[0]-B[0], C[1]-B[1])
b = (A[0]-C[0], A[1]-C[1])
c = (A[0]-B[0], A[1]-B[1])

#length with pythagoras
la = ((C[0]-B[0])**2 + (C[1]-B[1])**2)**0.5
lb = ((A[0]-C[0])**2 + (A[1]-C[1])**2)**0.5
lc = ((A[0]-B[0])**2 + (A[1]-B[1])**2)**0.5

raw_w_cos = (la / lc)

#Loop preconditions
base = mt.pi / 2
expo = 1
t = raw_w_cos ** expo
arc = base  
term = t

while abs(term) > 0.000001: 
    zaehler = 1                
    for i in range(1, expo, 2):      
      zaehler = zaehler * i

    nenner = 1
    for i in range(2, expo, 2):     
      nenner = nenner * i
    nenner = nenner * expo
    term = zaehler / nenner * t ** expo     
    arc = arc -term
    expo = expo + 2

degree = round(arc * 180 / mt.pi, 2)

print(f"{degree}°")





