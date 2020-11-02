name =input("Hi, What is your name? \n")

print("Hello,%s ! This is python program made by Sumit Deshmukh."%(name))
print("This program is used to solve quadratic equation.")

print('General form of equation is a*x^2+b*x+c=d')

print('Fill the values properly in integer format for all a,b,c&d')


c1=int(input('a='))
a=c1
x='x'

c2=int(input('b='))

c3=int(input('c='))

d=int(input('d='))

if d==0:
   
    print('Calculating for Solution ........')
    
    if 0<a<2:
        print('Your equation is  x^2+(%s)x+(%s)=0'%(c2,c3))
    else:
        print('Your equation is  (%s)x^2+(%s)x+(%s)=0'%(c1,c2,c3))

 #Formula 
#n=-b+-√b^2-4ac
 # d=2*a
 #x=n/d
 
    
    D=c2**2-4*c1*c3
    x1=(-c2+(D**0.5))/(2*c1)
    x2=(-c2-(D**0.5))/(2*c1)
    
    print("Roots are")
    
    print("x1=",x1)
    print("x2=",x2)
        
        
    print("The End")
        
elif d>=0:
    print('Solving...')
    
    if 0<a<2:
        print('Your equation is  x^2+(%s)x+(%s)=(%s)'%(c2,c3,d))
    else:
        print('Your equation is  (%s)x^2+(%s)x+(%s)=(%s)'%(c1,c2,c3,d))

    D=c3-d
    
    if 0<a<2:
        print('Equation becomes:  x^2+(%s)x+(%s)=0'%(c2,D))
    else:
        print('Equation becomes:  (%s)x^2+(%s)x+(%s)=0'%(c1,c2,D))
    
    
    D3=c2**2-4*c1*D
    x1=(-c2+(D3**0.5))/(2*c1)
    x2=(-c2-(D3**0.5))/(2*c1)
    
    print("Roots are")
    
    print("x1=",x1)
    print("x2=",x2)
        
        
        
    print("The End") 
 
 
    

elif d<=0:
    print('Solving...')
    
    if 0<a<2:
        print('Your equation is  x^2+(%s)x+(%s)=(%s)'%(c2,c3,d))
    else:
        print('Your equation is  (%s)x^2+(%s)x+(%s)=(%s)'%(c1,c2,c3,d))
        
    D=c3-d
    
    if 0<a<2:
        print('Equation becomes:  x^2+(%s)x+(%s)=0'%(c2,D))
    else:
        print('Equation becomes:  (%s)x^2+(%s)x+(%s)=0'%(c1,c2,D))
        
    D3=c2**2-4*c1*D
    x1=(-c2+(D3**0.5))/(2*c1)
    x2=(-c2-(D3**0.5))/(2*c1)
    
    print("Roots are")
    
    print("x1=",x1)
    print("x2=",x2)
    
        
    print("The End")    
        
    
 
 