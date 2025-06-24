from karel.stanfordkarel import *

#There are two way to solve this, usine a while loop
#or usin a For loop

def main():
    while beepers_present():
        move()

#def main():
    for i in range(6):
      if beepers_present():
       move()
    
    
        
        


# There is no need to edit code beyond this point

if __name__ == '__main__':
    main()