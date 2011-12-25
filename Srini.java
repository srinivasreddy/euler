import java.math.BigInteger;

public class Srini{

public void main(String [] args){
  
  BigInteger summation = new BigInteger();
  for(int i=1;i<=1000;i++)
     {
       BigInteger temp = new BigInteger();
       for(int j=1;j<=i;j++)
          {
           temp= temp.multiply(BigInteger.valueOf(i));           
          }
       summation = summation.add(temp);
     }
     System.out.println(summation.toString());  
}
}
