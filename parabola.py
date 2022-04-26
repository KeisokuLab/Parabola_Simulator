from cmath import cos
import math
import matplotlib.pyplot as plt

dt = 0.01
x = []
y = []
x.append(0)
y.append(0)
v0 = 50.0
theta = 45.0
g = 9.81

#半径 m
r = 0.005
A = math.pi * r * r

#密度
density = 350
density_air = 1.205
mass = (4/3)*math.pi*r*r*r*density

def ReCal(u):
    return r*2*u / (1.512*10**-5)

def CdCal(Re):
    return 24/Re + (2.6*(Re/5.0))/(1+(Re/5.0)**1.52) + 0.411*((Re/(2.63*10**5))**-7.94)/(1+(Re/(2.63*10**5))**-8.0) + (0.25*(Re/10**6)) / (1+(Re/10**6))

def DCal(u,Cd):
    return 0.5 * Cd * density_air * A * u * u

vx = []
vx.append(v0 * math.cos(math.pi * theta / 180))
vy = []
vy.append(v0 * math.sin(math.pi * theta / 180))
# ya -> y*
xa = 0
vxa = 0
ya = 0
vya = 0
Dx = []
Dy = []

Re0 = ReCal(v0)
Cd0 = CdCal(Re0)
Dx.append(-abs(DCal(v0,Cd0))*vx[0]/v0)
Dy.append(-abs(DCal(v0,Cd0))*vy[0]/v0)

for i in range(1000):
    vx.append(vx[i] + (Dx[i] / mass) * dt)
    vy.append(vy[i] - g * dt + (Dy[i] / mass) * dt)
    V = math.sqrt(vx[i+1] * vx[i+1] + vy[i+1] * vy[i+1])
    Re = ReCal(V)
    Cd = CdCal(Re)
    Dx.append(-abs(DCal(V,Cd)*vx[i+1]/V))
    Dy.append(-abs(DCal(V,Cd)*vy[i+1]/V))
    print(vx[i])
    
for i in range(1000):
    if y[i] < 0:
        break
    x.append(x[i] + (vx[i] + vxa)*dt/2)
    y.append(y[i] + (vy[i] + vya)*dt/2)
    xa = x[i] + dt * vx[i]
    xa_next = x[i+1] + dt * vx[i+1]
    vxa = (xa_next - xa) / dt
    ya = y[i] +  dt * vy[i]
    ya_next = y[i+1] + dt * vy[i+1]
    vya = (ya_next - ya) / dt

plt.plot(x, y)
plt.show()