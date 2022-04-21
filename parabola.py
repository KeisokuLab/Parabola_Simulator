from cmath import cos
import math
import matplotlib.pyplot as plt

dt = 0.01
x = []
y = []
x.append(0)
y.append(0)
v0 = 30.0
theta = 35.0
g = 9.81

#抗力係数
Cd = 0.47
#半径 m
r = 0.05
A = math.pi * r * r
#動粘度
vv = 15.12*10**-6
#密度
density = 1300
mass = (4/3)*math.pi*r*r*r*density

def DCal(Cd,u):
    return Cd*density*u*u*A/2
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
Re = 2*r*v0/vv
Cd = 24/Re
Dx.append(-abs(DCal(Cd,v0)*vx[0]/v0))
Dy.append(-abs(DCal(Cd,v0)*vy[0]/v0))

for i in range(300):
    vx.append(vx[i] - Dx[i] * dt / mass)
    vy.append(vy[i] - g * dt + Dy[i] * dt / mass)
    V = math.sqrt(vx[i+1] * vx[i+1] + vy[i+1] * vy[i+1])
    Re = 2*r*V/vv
    Cd = 24/Re
    Dx.append(-abs(DCal(Cd,V)*vx[i+1]/V))
    Dy.append(-abs(DCal(Cd,V)*vy[i+1]/V))

for i in range(300):
    x.append(x[i] + (vx[i] + vxa)*dt/2)
    y.append(y[i] + (vy[i] + vya)*dt/2)
    xa = x[i] + dt * vx[i]
    xa_next = x[i+1] + dt * vx[i+1]
    vxa = (xa_next - xa) / dt
    ya = y[i] +  dt * vy[i]
    ya_next = y[i+1] + dt * vy[i+1]
    vya = (ya_next - ya) / dt

print(Dx,Dy)

plt.plot(x, y)
plt.show()