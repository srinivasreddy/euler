def snake_sum(n):
    flag=1
    times=1
    for i  in range(n):
	if(flag==i and i<=times):           
           yield i
           flag=flag+2
           if(
           

def main():
    print sum(snake_sum(1024*1024))
     

if __name__=="__main__":
   main()


21 22  23  24  25 
20  7  8   9   10
19  6  1   2   11
18  5  4   3   12
17 16 15  14   13

