from decimal import Decimal
from fractions import Fraction

if __name__ =="__main__":
   listt=[]
   for denom in range(10,100):
       for num in range(10,denom):
               if(str(num)[1]==str(denom)[0]):                 
 		  xnum=int(str(num)[0])
		  xdenom=int(str(denom)[1])
                  if(xdenom!=0 and Fraction(num,denom)==Fraction(xnum,xdenom)):
                      listt.append(Fraction(num,denom))
   x = reduce(lambda x,y :x*y,(i.numerator for i in listt))
   y = reduce(lambda x,y :x*y,(i.denominator for i in listt))
   print Fraction(x,y).denominator
                      
      
                  


                     
       
