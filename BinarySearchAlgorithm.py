
import math

def BinarySearch (l,e):
   m=True
   l.sort()
  
   while m==True:
        l2=[]
        m1=float((len(l) - 1)/2) 
        m1=math.floor(m1)
        print(l[m1])
        if e > l[m1] : 
          for i in range (m1+1,len(l)):
              l2.append(l[i])
          l=list(l2)
        elif e < l[m1]:
          for i in range(0,m1):
                l2.append(l[i])
          l=list(l2)
         
        else:
            m=False
           
   



BinarySearch([12,5,6,324,75,40,21],5)


 



