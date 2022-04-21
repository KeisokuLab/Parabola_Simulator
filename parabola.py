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

vx = v0 * math.cos(math.pi * theta / 180)
vy = []
vy.append(v0 * math.sin(math.pi * theta / 180))
# ya -> y*
xa = 0
ya = 0
vya = 0

for i in range(430):
    xa = x[i] + vx * dt
    x.append(xa)
    vy.append(vy[i] - g * dt)

for i in range(430):
    y.append(y[i] + (vy[i] + vya)*dt/2)
    ya = y[i] +  dt * vy[i]
    ya_next = y[i+1] + dt*vy[i+1]
    vya = (ya_next - ya) / dt
    
plt.plot(x, y)
plt.show()