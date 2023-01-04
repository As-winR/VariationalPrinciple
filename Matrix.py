import scipy as sp
import numpy as np
a = 0
b = 5
N = 1000

h_bar_sq = 1
m = 1
del_x = (b - a) / N
pi_ss = float(np.pi**2/3)


# numbers = [[x for x in range(i*N + 1, N + i*N + 1)] for i in range(N)]  # for building a 123 matrix (remember what aswin said)

final = []


def mat(N):
    for j in range(N):
        tt = [0 for x in range(N - j)]
        a = [float((-1)**(i - j) * (2 / ((i - j) ** 2))) for i in range(j)]
        a.extend(tt)
        final.append(a)

    return final


t_low = np.array(mat(N))
const = h_bar_sq / (2 * m * (del_x**2))
t_matrix = (t_low + pi_ss*np.identity(N) + t_low.T)*const

v_matrix = np.diagflat([(i*del_x)**2 for i in range(1, N+1)])

h_matrix = t_matrix + v_matrix

eval, efunc = np.linalg.eig(h_matrix)







