

def addition(n1,n2):
    if type(n1) in [int,float,complex] and type(n2) in [int,float,complex]:
        if n1<=0 or n2<=0:
            return 'Number shud be greater than zero'
        return n1+n2
    else:
        return 'Invalid Input'