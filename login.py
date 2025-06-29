

USER = "Admin"
PASS = "Admin123"

def authenticate_user(username,password):       #business functionality -- business code..
    if username:
        if password:
            if USER==USER and PASS==password:
                return 'Login Successful'
            else:
                return 'Invalid Crendentails'
        else:
            return 'Password Cannot Be Empty...'
    else:
        return 'Username cannot be Empty...'


def addition(n1,n2):
    sum = 0
    if n1>0 and n2>0:
        sum = n1+n2
        return sum

