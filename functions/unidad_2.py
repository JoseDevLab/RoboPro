import numpy as np
from math import cos, sin, atan2, radians, degrees, floor, sqrt

def longitudes():
    L1 = 170
    L2 = 75
    L4 = 70
    return L1, L2, L4

def limitesQ():
    q1Min = -180
    q1Max = 180
    q2Min = 0
    q2Max = 280
    q3Min = 0
    q3Max = 420
    q4Min = -180
    q4Max = 180
    qp1Max = 180
    qp2Max = 200
    qp3Max = 200
    qp4Max = 180
    qpp1Max = 180
    qpp2Max = 200
    qpp3Max = 200
    qpp4Max = 180
    qMin = [q1Min,q2Min,q3Min,q4Min]
    qMax = [q1Max,q2Max,q3Max,q4Max]
    qpMax = [qp1Max,qp2Max,qp3Max,qp4Max]
    qppMax = [qpp1Max,qpp2Max,qpp3Max,qpp4Max]
    return qMin,qMax,qpMax,qppMax
    
def cinematicaDirecta(q1:float,q2:float,q3:float,q4:float):
    L1,L2,L4=longitudes()
    q1=radians(q1)
    q4=radians(q4)
    T = np.array([[cos(q1)*cos(q4), -cos(q1)*sin(q4), -sin(q1), -L4*sin(q1)-L2*cos(q1)-q3*sin(q1)],
                  [cos(q4)*sin(q1), -sin(q1)*sin(q4),  cos(q1),  L4*cos(q1)-L2*sin(q1)+q3*cos(q1)],
                  [       -sin(q4),         -cos(q4),        0,                             L1+q2],
                  [              0,                0,        0,                                 1]])
    return T

def cinematicaInversa(T:np.ndarray):
    L1,_,L4=longitudes()
    nz = T[2,0]
    oz = T[2,1]
    ax = T[0,2]
    ay = T[1,2]
    px = T[0,3]
    py = T[1,3]
    pz = T[2,3]
    q1 = atan2(-ax,ay)
    q2 = pz-L1
    q3 = cos(q1)*py-sin(q1)*px-L4
    q4 = atan2(-nz,-oz)
    q1 = degrees(q1)
    q4 = degrees(q4)
    x = floor((abs(q1)-180)/360)*360 + 360
    if q1 <= -180:
        q1 = x + q1
    else:
        if q1 > 180:
            q1 = q1 - x
    x = floor((abs(q4)-180)/360)*360 + 360
    if q4 <= -180:
        q4 = x + q4
    else:
        if q4 > 180:
            q4 = q4 - x
    return q1,q2,q3,q4

def generaMTH(P,q4):
    q4 = radians(q4)
    _,L2,_=longitudes()
    px = P[0]
    py = P[1]
    q1 = atan2(py,px)-atan2(sqrt(py**2+px**2-L2**2),-L2)
    R = np.array([[cos(q1)*cos(q4), -cos(q1)*sin(q4), -sin(q1)],
                  [cos(q4)*sin(q1), -sin(q1)*sin(q4),  cos(q1)],
                  [       -sin(q4),         -cos(q4),        0]])
    P = np.array([P]).T
    T = np.vstack([np.hstack([R, P]), [0, 0, 0, 1]])
    T = np.round(T,2)
    return T

def interpolarLinealR3(PuntosR3:list,nPuntos:int):
    puntos = np.array(PuntosR3)
    n = puntos.shape[1]
    q4 = puntos[3,:]
    ti = puntos[-1,:]
    puntos = puntos[0:3,:]
    V = np.zeros((3,nPuntos-1))
    m = np.zeros(nPuntos-1)
    b = np.zeros(nPuntos-1)
    tm = np.linspace(ti[0],ti[-1],nPuntos)
    for i in range(n-1):
        V[:,i] = puntos[:,i+1]-puntos[:,i]
        m[i] = (q4[i+1]-q4[i])/(ti[i+1]-ti[i])
        b[i] = q4[i]-m[i]*ti[i]
    puntosInt = np.zeros((3,nPuntos))
    q4Int = np.zeros(nPuntos)
    i = 0
    for j in range(nPuntos):
        t = tm[j]
        if t > ti[i+1]:
            i+=1
        alpha = (t-ti[i])/(ti[i+1]-ti[i])  # alpha es un valor entre 0 y 1
        puntosInt[:,j] = puntos[:,i]+alpha*V[:,i]
        q4Int[j] = m[i]*t+b[i]
        
    PuntosR3Int = np.vstack((puntosInt,q4Int,tm))
    return PuntosR3Int.tolist()
        
def interpoladorLineal(qi:list,ti:list,nPuntos:int):
    n = len(qi)
    m = np.zeros(nPuntos-1)
    b = np.zeros(nPuntos-1)
    tm = np.linspace(ti[0],ti[-1],nPuntos)
    for i in range(n-1):
        m[i] = (qi[i+1]-qi[i])/(ti[i+1]-ti[i])
        b[i] = qi[i]-m[i]*ti[i]
    qInt = np.zeros(nPuntos)
    qpInt = np.zeros(nPuntos)
    i = 0
    for j in range(nPuntos):
        t = tm[j]
        if t > ti[i+1]:
            i+=1
        qInt[j] = m[i]*t+b[i]
        qpInt[j] = m[i]
    return qInt, qpInt, tm

def v_criterioHeuristico(t,q):
    n = len(t)
    qd = np.zeros(n)
    for i in range(1,n-1):
        if (q[i]-q[i-1]< 0 and q[i+1]-q[i] > 0) or (q[i]-q[i-1] > 0 and q[i+1]-q[i] < 0):
            qd[i] = 0
        elif np.sign(q[i]-q[i-1])==np.sign(q[i+1]-q[i]) or q[i-1]==q[i] or q[i]==q[i+1]:
            qd[i] = (1/2)*(((q[i+1]-q[i])/(t[i+1]-t[i]))+((q[i]-q[i-1])/(t[i]-t[i-1])))
    return qd

def V_AceleracionContinua(t, q):
    n = len(t)
    qp = np.zeros(n)
    A = np.zeros((n, n))
    B = np.zeros(n)

    for i in range(1, n-1):
        ti0 = t[i-1]
        ti = t[i]
        ti1 = t[i+1]
        qi0 = q[i-1]
        qi = q[i]
        qi1 = q[i+1]
        abc = [2 / (ti - ti0), 4 / (ti - ti0) - 4 / (ti - ti1), -2 / (ti - ti1)]
        A[i, i-1:i+2] = abc
        B[i] = -(6 * (qi - qi1)) / (ti - ti1) ** 2 + (6 * (qi - qi0)) / (ti - ti0) ** 2
    qp[1:n-1] = np.linalg.solve(A[1:n-1, 1:n-1], B[1:n-1])
    return qp.tolist()

def interpoladorCubico(t,q,op_v,qd=None):
    n = len(t)
    if op_v==0:
        qd=qd
    elif op_v==1:
        qd = v_criterioHeuristico(t,q)
    elif op_v==2:
        qd = V_AceleracionContinua(t,q)
    ti = np.array(t)[0:n-1].tolist()
    tim1 = np.array(t)[1:n].tolist()
    a = np.zeros(n-1).tolist()
    b = np.zeros(n-1).tolist()
    c = np.zeros(n-1).tolist()
    d = np.zeros(n-1).tolist()
    
    for i in range(n-1):
        a[i] = q[i]
        b[i] = qd[i]
        T = t[i+1]-t[i]
        c[i] = (3/(T**2))*(q[i+1]-q[i])-(1/T)*(qd[i+1]+2*qd[i])
        d[i] = -(2/(T**3))*(q[i+1]-q[i])+(1/(T**2))*(qd[i+1]+qd[i])
    return ti,tim1,a,b,c,d

def interpoladorCubicoMuestreo(t,nPuntos,q,op_v,qp=None):
    ti,tim1,a,b,c,d = interpoladorCubico(t,q,op_v,qp)
    tInt = np.linspace(t[0],t[-1],nPuntos)
    qInt = np.zeros(nPuntos).tolist()
    qpInt = np.zeros(nPuntos).tolist()
    qppInt = np.zeros(nPuntos).tolist()
    qpppInt = np.zeros(nPuntos).tolist()
    
    i=0
    for j in range(nPuntos):
        tm=tInt[j]
        if tm > t[i+1]:
            i+=1
        qInt[j]=a[i]+b[i]*(tm-ti[i])+c[i]*(tm-ti[i])**2+d[i]*(tm-ti[i])**3
        qpInt[j]=b[i]+2*c[i]*(tm-ti[i])+3*d[i]*(tm-ti[i])**2
        qppInt[j]=2*c[i]+6*d[i]*(tm-ti[i])
        qpppInt[j]=6*d[i]
    return tInt,qInt,qpInt,qppInt,qpppInt

def int_lineal_vec_t(qi:float,qf:float,vmax:float,vec_t:list,ti:float,tf=None):
    nPuntos = len(vec_t)
    tm = np.array(vec_t)-ti
    q = np.zeros(nPuntos)
    qp = np.zeros(nPuntos)
    dqi = qf-qi
    s = np.sign(dqi)
    if tf==None:
        V = s*vmax
        T = dqi/(V)
    else:
        T = tf-ti
        V = dqi/T
    # b = qi-s*V*ti
    for i in range(nPuntos):
        t = tm[i]
        if t<=0:
            q[i] = qi
        elif t>=T:
            q[i] = qf
        else:
            q[i] = V*t+qi
            qp[i] = V
    return q.tolist(),qp.tolist()

def int_trapezoidal_tmin(qi, qf, a, vmax, ajustar=False):
    tau = vmax/a
    dq = qf-qi
    s = np.sign(dq)
    T = s*(dq/vmax)+tau
    if 2*tau>T:
        if s==0:
            T=0
        else:
            if ajustar:
                T=2*tau
            else:
                T=abs(sqrt((4*dq)/(s*a)))
    return T
    
def int_trapezoidal_vec_t(qi:float,qf:float,a:float,vmax:float,vec_t:list,ti:float,tf:float=None):
    nPuntos = len(vec_t)
    tm = np.array(vec_t)-ti
    q = np.zeros(nPuntos)
    qp = np.zeros(nPuntos)
    qpp = np.zeros(nPuntos)
    dqi = qf-qi
    s = np.sign(dqi)
    if tf==None:
        V = vmax
        T = int_trapezoidal_tmin(qi, qf, a, V)
    else:
        T = tf-ti
        if T**2<(4*s*dqi)/a:
            raise ValueError('Se requiere de más tiempo para realizar el movimiento')
        V = (T-(sqrt(T**2-(4*s*dqi)/a)))/(2/a)
    tau = V/a
    for i in range(nPuntos):
        t = tm[i]
        if t<=0:
            q[i] = qi
        elif t>=T:
            q[i] = qf
        else:
            if 2*tau<=T:
                if t<=tau:
                    q[i] = qi+s*(a/2)*t**2
                    qp[i] = s*a*t
                    qpp[i] = s*a
                elif tau<t and t<=T-tau:
                    q[i] = qi-s*((V**2)/(2*a))+s*V*t
                    qp[i] = s*V
                elif T-tau<t and t<T:
                    q[i] = qf+s*(-((a*T**2)/2)+a*T*t-(a/2)*t**2)
                    qp[i] = s*(a*T - a*t)
                    qpp[i] = -s*a
            else:
                if t<=T/2:
                    q[i] = qi+s*(a/2)*t**2
                    qp[i] = s*a*t
                    qpp[i] = s*a
                elif T/2<t and t<T:
                    q[i] = qf+s*(-((a*T**2)/2)+a*T*t-(a/2)*t**2)
                    qp[i] = s*(a*T - a*t)
                    qpp[i] = -s*a
    return q.tolist(),qp.tolist(),qpp.tolist()
