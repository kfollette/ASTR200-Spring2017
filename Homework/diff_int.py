 def diff_int(d=0.01*u.cm,a=0.001*u.cm,wl=400*u.nm):
    '''
    function that returns the intensity of a double slit interference pattern
    '''
    theta = arange(-10,10,1e-5)*u.degree
    x = pi*a*sin(theta)/wl*u.radian
    xnew = x.decompose()
    i_single = (sin(xnew)/xnew)**2
    
    y = pi*d*sin(theta)/wl*u.radian
    ynew = y.decompose()
    i_double = (cos(ynew))**2

    I = i_single*i_double
    
    plot(theta,I)
    return
