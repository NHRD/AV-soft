import numpy as np

dt = 0.5
Fk = np.array([[1, dt], [0, 1]])
Gk = np.array([[0], [dt]])
Qk = np.array([[0.1, 0], [0, 0.1]])
x0 = np.array([[0], [5]])
P0 = np.array([[0.01, 0], [0, 1]])
u0 = np.array([[-2]])
Hk = np.array([[1, 0]])
Rk = np.array([[0.05]])
y1 = np.array([[2.2]])

xprev = Fk @ x0 + Gk @ u0
Pk = Fk @ P0 @ Fk.T + Qk
K = Pk @ Hk.T @ np.linalg.inv(Hk @ Pk @ Hk.T + Rk)
xk = xprev + K @ (y1 - Hk @ xprev)

print(xk)