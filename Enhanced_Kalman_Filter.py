import numpy as np

dt = 0.5
u0 = -2
y1 = np.pi/6  # 30度
S = 20
D = 40
x0 = np.array([[0], [5]])
p0 = x0[0, 0]

Fk = np.array([[1, dt], [0, 1]])
Lk = np.eye(2)
Hk = np.array([[S/((D - p0)**2 + S**2), 0]])
M = np.array([[1]])
P = np.array([[0.01, 0], [0, 1]])