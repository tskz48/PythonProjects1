
import os

filepath=input("Specify a file directory.")
p = input("Type in a pattern.")
os.chdir(filepath) #sets new working directory
for name in os.listdir(filepath):   
    os.rename(str(name),str(p))
    

    


       
