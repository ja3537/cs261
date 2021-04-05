# -*- coding: utf-8 -*-
"""
Created on Mon Apr 13 19:46:08 2020

@author: Joseph
"""

def extended_euclid(a,b):
    coeff=[]
    A = max(a,b)
    B = min(a,b)
    r= A%B
    
    if r== 0:
        if max(a,b)== a:
            return (B,0,1)
        else:
            return (B,1,0)
    
    if B%r== 0:
        if max(a,b)== a:
            return (r,1,-(A//B))
        else:
            return (r,-(A//B),1)
    
    while A%B!= 0:
        coeff.append(-(A//B))
        r= A%B
        A= B
        B= r
        
    gcd= B
    Acoeff= []
    Bcoeff= []
    Acoeff.append(1)
    Acoeff.append(coeff[1])
    Bcoeff.append(coeff[0])
    Bcoeff.append(coeff[0]* coeff[1]+ 1)
    
    for i in range(2,len(coeff)):
        Acoeff.append(Acoeff[i-2]+ coeff[i]*Acoeff[i-1])
        Bcoeff.append(Bcoeff[i-2]+ coeff[i]*Bcoeff[i-1])
        
    if max(a,b)== a:
        return (gcd, Acoeff[-1], Bcoeff[-1])
    else:
        return (gcd, Bcoeff[-1], Acoeff[-1])
    
    
continuevar = 'y'

while continuevar != "n":
    A = input('Please insert your first number:')
    B = input('Please insert your second number:')
    print('(gcd, s, t) = '+ str(extended_euclid(int(A),int(B))))
    continuevar = input('Continue? (y/n)')
    
input('Press ENTER to exit')
    