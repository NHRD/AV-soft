import numpy as np

dt = 0.5
u0 = -2
y1 = np.pi/6  # 30度
S = 20
D = 40
x0 = np.array([[0], [5]])
P = np.array([[0.01, 0], [0, 1]])
Fk = np.array([[1, dt], [0, 1]])
Lk = np.eye(2)
Gk = np.array([[0], [dt]])
Qk = np.array([[0.01, 0], [0, 0.01]])
Rk = np.array([[0.01]])

x_check = Fk @ x0 + Gk * u0
p_check = x_check[0, 0]
Hk = np.array([[S/((D - p_check)**2 + S**2), 0]])
Mk = np.array([[1]])
y_check = np.arctan(S / (D - p_check))   # スカラー
y_check = y1 - y_check
P_check = Fk @ P @ Fk.T + Lk @ Qk @ Lk.T
Kk = P_check @ Hk.T @ np.linalg.inv(Hk @ P_check @ Hk.T + Mk @ Rk @ Mk.T)
x_est = x_check + Kk @ (y_check - np.arctan(S / (D - p_check)))
P_est = (np.eye(2) - Kk @ Hk) @ P_check

print(x_est, P_est)