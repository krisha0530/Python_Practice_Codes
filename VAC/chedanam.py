#CHEDANAM PYTHON CODE
def chedanam(a,b,c):
    tp=a*c
    limit =abs(tp)+abs(b)+1
for i in range(-limit,limit):
    j=b-i
    if i * j == tp:
        print("split",b,"int",i,"and",j)
        print("grouping:(",a,"x^2+",i,"x)+(",i,"x+",c,")")
    break
chedanam(1,5,6)
# CODED BY KRISHA!
