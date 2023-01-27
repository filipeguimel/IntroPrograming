A=int(input())
L=int(input())
P=int(input())
H=int(input())

x1 = (A+L+abs(A-L))/2
x2 = (A+P+abs(A-P))/2
x3 = (L+P+abs(L-P))/2

valores=(x1,x2,x3)
maior=int(max(valores)*H)

print (maior)