import numpy as np

dt = 0.5
Fk = np.array([[1, dt], [0, 1]]) #xは位置および速度の2x1のため2x2の行列
Gk = np.array([[0], [dt]]) #uは加速度のため2x1で、計算結果は速度
Qk = np.array([[0.1, 0], [0, 0.1]])
x0 = np.array([[0], [5]]) #初期は位置0、加速度5m/s^2
P0 = np.array([[0.01, 0], [0, 1]])
u0 = np.array([[-2]]) #加速度は-2m/s^2
Hk = np.array([[1, 0]])
Rk = np.array([[0.05]])
y1 = np.array([[2.2]])

xprev = Fk @ x0 + Gk @ u0 #Fk @ xn + Gk @ u0で前回値xk-1をxprevとして算出
Pk = Fk @ P0 @ Fk.T + Qk #Pkはxk-1の誤差共分散行列
K = Pk @ Hk.T @ np.linalg.inv(Hk @ Pk @ Hk.T + Rk) #KはPkを最小にするためのゲイン行列、これがカルマンゲイン
xk = xprev + K @ (y1 - Hk @ xprev) #xの最新xkはxprevに実測と前回予測値の差分y1-Hk @ xprevにカルマンゲインKを掛けたものを足す。

np.set_printoptions(precision=2, suppress=True)
print(xk)