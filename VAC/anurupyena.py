#ANURUPYENA PYTHON CODE

def anurupyena(a1,b1,c1,a2,b2,c2):
    ratio_x=a1/a2
    ratio_y=b1/b2
    ratio_c=c1/c2

# CODED BY KRISHA!
  
    if ratio_x==ratio_c:
        y=0
        x=c1/a1
        return x,y
    
    elif ratio_y==ratio_c:
        x=0
        y=c1/b1
        return x,y
    else:
        return "Not Applicable"
    print(anurupyena(3,7,12,9,5,36))
