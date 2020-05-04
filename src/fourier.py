import numpy as np

class Fourier():
    def __init__(self, data, N):
        self.data = data
        self.N = N

    def integrate(self, f, a, b):
        s = 0
        dt = 0.001
        return sum(f(t)*dt for t in np.arange(a, b, dt))

    def nth_coef(self, data, n):
        f = lambda t : data.get(t) * np.exp(-2 * np.pi * n * t * 1j)
        return self.integrate(f, 0, 1)

    def sample(self):
        coef = [{'n': 0, 'c': self.nth_coef(self.data, 0)}]
        for n in range(1, self.N):
            coef.append({'n': n, 'c': self.nth_coef(self.data, n)})
            coef.append({'n': -n, 'c': self.nth_coef(self.data, -n)})
        return coef
