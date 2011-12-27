from datetime import  date

if __name__ =="__main__":
   total=0
   for year in range(1,101):
       for month in range(1,13):
           d=date(1900+year,month,1)
           if(d.weekday()==1):
              total=total+1
   print total

