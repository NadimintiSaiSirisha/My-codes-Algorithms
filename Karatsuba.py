def siri(x,y):
                if len(str(x)) == 1 or len(str(y)) == 1:
                    return x*y
                else:
                    n = max(len(str(x)),len(str(y)))
                    nby2 = n / 2
                    
                    a = x / 10**(nby2)
                    b = x % 10**(nby2)
                    c = y / 10**(nby2)
                    d = y % 10**(nby2)
                    
                    ac = siri(a,c)
                    bd = siri(b,d)
                    ad_plus_bc = siri(a+b,c+d) - ac - bd
            
                    prod = ac * 10**(2*nby2) + (ad_plus_bc * 10**nby2) + bd

                    return prod

a=input("Enter first number ")
b=input("Enter second number ")
print(siri(a,b))
