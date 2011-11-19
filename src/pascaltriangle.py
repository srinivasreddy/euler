def pascal_triangle(n):
    yield [1]
    if(n==0):
       return
    yield [1,1]
    temp=[1,1]
    counter=1
    while counter<n:
          k=0
          another=[]
          for i in temp:
              another.append(i+k)
              k=i
          another.append(1)
          temp=another
          counter=counter+1
          yield another

##usage of pascal triangle..

for i in pascal_traingle(8):
    print i
"""
[1]
[1, 1]
[1, 2, 1]
[1, 3, 3, 1]
[1, 4, 6, 4, 1]
[1, 5, 10, 10, 5, 1]
[1, 6, 15, 20, 15, 6, 1]
[1, 7, 21, 35, 35, 21, 7, 1]
"""
