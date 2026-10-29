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

#length = √(x² + y²)
la = ((C[0]-B[0])**2 + (C[1]-B[1])**2)**0.5
lb = ((A[0]-C[0])**2 + (A[1]-C[1])**2)**0.5
lc = ((A[0]-B[0])**2 + (A[1]-B[1])**2)**0.5

raw_w_cos = (la / lc)

#stuff for arccos
counter = 1

# to get into loop
fresh = True
arc = mt.pi / 2
term = raw_w_cos
dez = 1


term = dcounter
dcounter = 1

while dez > 0.000001 or fresh:
    fresh = False
    term = term ** counter
    arc = arc - term
    dez = arc % 1
    counter = counter + 2
    dcounter = dcounter 

print (arc)
