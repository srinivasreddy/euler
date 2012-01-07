

if __name__ =="__main__":
   triangle=[]
   pentagonal=[]
   hexagonal=[]
   i=1
   while True:
         t=(i*(i+1))/2
         triangle.append(t)
	 pentagonal.append((i*(3*i-1))/2)
	 hexagonal.append(i*(2*i-1))
         #print t,(i*(3*i-1))/2,i*(2*i-1)
         #print t in pentagonal
         if((t in pentagonal) and (t in hexagonal)):
             print t
             if (t!=1 and t!=40755):
                 break
         i=i+1

          
  
