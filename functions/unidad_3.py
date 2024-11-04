from numpy import linspace, zeros_like, random, repeat,ones_like
from control import forced_response, TransferFunction, series, feedback, parallel, pade, negate, sample_system

def generarTrayectoria(tSim,nPuntos):
    t=linspace(0, tSim, nPuntos)
    qpp = zeros_like(t)
    qpp[t >= 0] += 1  # Primer escalón
    qpp[t >= 1] -= 1  # Segundo escalón
    qpp[t >= 4] -= 1  # Tercer escalón
    qpp[t >= 5] += 1  # Cuarto escalón
    
    integral = TransferFunction([1],[1,0])
    
    _, qp = forced_response(integral, T=t, U=qpp)
    _, q = forced_response(integral, T=t, U=qp)
    
    return t,q,qp,qpp

def SControlFF(Je,Be,Ke,qp,qpp):
    return (1/Ke)*((qp*Be)+(qpp*Je))

def controlPrealimentado(tSim,Je,Be,Ke,perturb=False,APerturb=None):
    t,q,qp,qpp=generarTrayectoria(tSim,1000)
    if perturb:
        perturbacion=random.uniform(-APerturb, APerturb, 100)
        perturbacion = repeat(perturbacion, len(t) // len(perturbacion))
    else:
        perturbacion=zeros_like(t)
    J = 1
    B = 10
    K = 1
    F1 = SControlFF(Je,Be,Ke,qp,qpp)
    senial = (F1*K)-perturbacion
    integral = TransferFunction([1],[1,0])
    planta = TransferFunction([1],[J,B])
    _,salida = forced_response(series(planta,integral),t,senial)
    return t,q,salida,perturbacion

def controlRealimentado(tSim,Kp,Ki,Kd,perturb=False,APerturb=None):
    J=1
    B=10
    K=1
    proporcional=TransferFunction([Kp],[1])
    integral=TransferFunction([Ki],[1,0])
    derivativo=TransferFunction([Kd,0],[1])
    controlador=parallel(proporcional,integral,derivativo)
    g_K=TransferFunction([K],[1])
    t=linspace(0,tSim,1000)
    U=ones_like(t)
    if perturb:
        num_d,den_d=pade(100,50)
        perturbacion=series(TransferFunction(num_d,den_d),TransferFunction([APerturb],[1]))
        tf1=parallel(negate(perturbacion),series(controlador,g_K))
        _,P=forced_response(perturbacion,t,U)
    else:
        P=zeros_like(t)
        tf1=series(controlador,g_K)
    lazo1=series(tf1,TransferFunction([1],[J,B]),TransferFunction([1],[1,0]))
    # H = TransferFunction([1],[1])
    sistema=feedback(lazo1)
    _,Y=forced_response(sistema,t,U)
    return t,U,Y,P

def controlRealimentadoD(tSim,Kp,Ki,Kd,ref,perturb=False,tPer=None,APerturb=None):
    J=1
    B=10
    K=1
    t=linspace(0,tSim,1000)
    U=ones_like(t)
    U[:]=ref
    U[0]=0
    Ts=t[1]-t[0]
    perturbacion=zeros_like(t)
    if perturb:
        perturbacion[t>=tPer] = APerturb
    Y = zeros_like(t)
    planta=series(TransferFunction([1],[J,B]),TransferFunction([1],[1,0]))
    plantaD=sample_system(planta, Ts, method='zoh')
    num=plantaD.num[0][0]
    den=plantaD.den[0][0]
    
    Kp = max(Kp, 2.7755575615628914e-17)
    Ki = max(Ki, 2.7755575615628914e-17)
    Kd = max(Kd, 2.7755575615628914e-17)
    Kc=Kp
    Ti = Kc / Ki
    Td = Kd / Kc
    Kpd = Kc-((Kc*Ts)/(2*Ti))   #Constante proporcional en tiempo discreto.
    Kid = Kp / (Ti * Ts)        #Constante integral en tiempo discreto.
    Kdd = (Kp * Td )/ Ts        #Constante derivativa en tiempo discreto.
    u1=0
    e1=0
    e2=0
    x1=0
    y0=0
    y1=0
    y2=0
    for i in range(1,len(t)):
        e0=U[i]-y0
        u0=u1+Kpd*(e0-e1)+Kid*Ts*e0+Kdd*((e0-2*e1+e2)/Ts)
        u1=u0
        e2=e1
        e1=e0
        x0=u0*K-perturbacion[i]
        y0=num[0]*x0+num[1]*x1-den[1]*y1-den[2]*y2
        y2=y1
        y1=y0
        x1=x0
        Y[i]=y0
    return t,U,Y,perturbacion

def prealimentadoMRealimentado(tSim,Kp,Ki,Kd,Je,Be,Ke,perturb=False,APerturb=None):
    J=1
    B=10
    K=1
    t,q,qp,qpp=generarTrayectoria(tSim,1000)
    U=q
    U[0]=0
    Ts=t[1]-t[0]
    if perturb:
        perturbacion=random.uniform(-APerturb, APerturb, tSim*10)
        perturbacion = repeat(perturbacion, len(t) // len(perturbacion))
    else:
        perturbacion=zeros_like(t)
    Y = zeros_like(t)
    planta=series(TransferFunction([1],[J,B]),TransferFunction([1],[1,0]))
    plantaD=sample_system(planta, Ts, method='zoh')
    num=plantaD.num[0][0]
    den=plantaD.den[0][0]
    
    Kp = max(Kp, 2.7755575615628914e-17)
    Ki = max(Ki, 2.7755575615628914e-17)
    Kd = max(Kd, 2.7755575615628914e-17)
    Kc=Kp
    Ti = Kc / Ki
    Td = Kd / Kc
    Kpd = Kc-((Kc*Ts)/(2*Ti))   #Constante proporcional en tiempo discreto.
    Kid = Kp / (Ti * Ts)        #Constante integral en tiempo discreto.
    Kdd = (Kp * Td )/ Ts        #Constante derivativa en tiempo discreto.
    u1=0
    e1=0
    e2=0
    x1=0
    y0=0
    y1=0
    y2=0
    for i in range(1,len(t)):
        e0=U[i]-y0
        u0=u1+Kpd*(e0-e1)+Kid*Ts*e0+Kdd*((e0-2*e1+e2)/Ts)
        u1=u0
        e2=e1
        e1=e0
        x0=(u0+(1/Ke)*(Je*qpp[i]+Be*qp[i]))*K-perturbacion[i]
        y0=num[0]*x0+num[1]*x1-den[1]*y1-den[2]*y2
        y2=y1
        y1=y0
        x1=x0
        Y[i]=y0
    return t,U,Y,perturbacion
