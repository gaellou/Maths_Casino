from math import *
from random import *

def poisson(k,m):
    """poisson(k,m): donne la probabilité d'avoir k évènements distribués selon une loi de Poisson de paramètre m"""
    p=e**(-m)
    for i in range(0,k):
        p*=m/k
        k-=1
    return p

def binom(k,n,p):
    """binom(k,n,p): probabilité d'avoir k réussite(s) dans n évènements indépendants, chaque évènement ayant une probabilité p% de réussite"""
    if k==n:
        return p**n
    if p==0:
        return 0.0
    if p==1.0:
        # NB: le cas k==n a déjà été traité plus haut
        return 0.0
    q=1-p
    if k==0:
        return q**n
    j1=k
    j2=n-k
    xmin=1.0e-200
    x=1.0
    for i in range(0,k):
        x*=n/k
        while (x>xmin) and (j1>0):
            x*=p
            j1-=1
        while (x>xmin) and (j2>0):
            x*=q
            j2-=1
        n-=1
        k-=1
    return x*(p**j1)*(q**j2)

def xgauss(p,m,s):
    """xgauss(p,m,s): renvoie la variable x distribuée selon une LN(m,s), et correspondant à une probabilité donnée p"""
    return m+s*xgaussred(p)

def xgaussred(p):
    """xgaussred(p): renvoie la variable x distribuée selon une LNR, et correspondant à une probabilité donnée p"""
    if p==0.5:
        return 0.0
    if p==0.0:
        return -7.56
    if p==1.0:
        return +7.56
    if p>0.5:
        pc=p
    else:
        pc=1-p
    du=1/2000
    eps=1.0E-15
    k=1/sqrt(2*pi)
    u1=0.0
    f1=k
    p1=0.5
    while True:
        u2=u1+du
        f2=k*exp(-0.5*u2*u2)
        s=(f1+f2)*0.5*du
        p2=p1+s
        if abs(p2-pc)<eps:
            break
        if ((p1<pc) and (p2<p1)) or  ((p1>pc) and (p2>p1)):
            # =on est en train de s'éloigner du point recherché
            du=-du/2
        u1=u2
        f1=f2
        p1=p2
    if p>0.5:
        return u2
    else:
        return -u2


def hpoisson(m,nb=0):
    """hpoisson(m,nb=0): Génération de valeurs tirées au hasard selon une distribution de Poisson"""
    def _hpoisson(m):
        ph=random()
        k=0
        pc=poisson(k,m)
        while ph>pc:
            k+=1
            pc+=poisson(k,m)
        return k

    if nb==0:
        return _hpoisson(m%38)
    else:
        R=[]
        for j in range(0,nb):
            R.append(_hpoisson(m)%38)
        return R

def hgauss(m=19,s=5,n=1):
    """hgauss(m,s): renvoie une valeur au hasard de la variable x distribuée selon une LN(m,s)"""
    if n==1:
        return xgauss(random(),m,s)
    else:
        L=[]
        for i in range(0,n):
            L.append(xgauss(random(),m,s))
            return L


def hbinom(n,p,nb=0):
    """hbinom(n,p,nb=0): Génération de valeurs tirées au hasard selon une distribution binomiale"""
    def _hbinom(n,p):
        ph=random.random()
        i=0
        pc=binom(i,n,p)
        while ph>pc:
            i+=1
            pc+=binom(i,n,p)
            return i
        if nb==0:
            return int(hbinom(n,p))
        else:
            R=[]
            for j in range(0,nb):
                R.append(_hbinom(n,p))
            return int(R)

def bernoulli(p) :
    for i in range (0,1) :
        t=random()
        if t<p :
            c=c+1
    return c
