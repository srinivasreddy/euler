import java.math.BigInteger;

import java.util.ArrayList;

public class FortyFive
{
 public static ArrayList<Integer> triangle = new ArrayList<Integer>(); 
 public static  ArrayList<Integer> pentagonal = new ArrayList<Integer>(); 
public static  ArrayList<Integer> hexagonal = new ArrayList<Integer>(); 

 public static void main(String [] args) {
   
      for(int i=1;i<=285;i++)
        triangle.add((i*(i+1))/2);
      for(int i=1;i<=285;i++)
        pentagonal.add((i*(3*i-1))/2);
      for(int i=1;i<=285;i++)
        hexagonal.add(i*(2*i-1));
        
      for(int i=286;;i++){           
          int temp=i*(i+1)/2;
          if(pentagonal.contains(temp) && hexagonal.contains(temp))
            {
              System.out.println(temp);
              System.out.println(i);
              break;
            }
            else
            {
             int  stud =i*(i+1)/2;
             triangle.add(stud);
             stud = (i*(3*i-1))/2;
             pentagonal.add(stud);
	     stud = i*(2*i-1);
             hexagonal.add(stud);
             }       

      } 
     
    
 }
}
