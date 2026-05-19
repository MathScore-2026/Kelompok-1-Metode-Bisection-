import matplotlib.pyplot as plt

class Bisection:
    def __init__(self, f, a, b, tol=1e-6, max_iter=100):
        self.f = f
        self.a = a
        self.b = b
        self.tol = tol
        self.max_iter = max_iter
        self.history = []

    def check_condition(self):
        return self.f(self.a) * self.f(self.b) < 0

    def solve(self):
        if not self.check_condition():
            raise ValueError("Syarat tidak terpenuhi")

        a, b = self.a, self.b

        for i in range(self.max_iter):
            c = (a + b) / 2
            fc = self.f(c)

            self.history.append((i+1, a, b, c, fc))

            if abs(fc) < self.tol:
                return c

            if self.f(a) * fc < 0:
                b = c
            else:
                a = c

        return c

    def print_table(self):
        print("Iter | a | b | c | f(c)")
        for row in self.history:
            print(row)

    def plot(self):
        x = [i/10 for i in range(int(self.a*10), int(self.b*10))]
        y = [self.f(i) for i in x]

        plt.plot(x, y)
        plt.axhline(0)
        plt.title("Grafik Fungsi")
        plt.show()


def f(x):
    return x**2 - 4

b = Bisection(f, 0, 3)
akar = b.solve()

b.print_table()
print("Akar:", akar)
b.plot()


def g(x):
    return x**3 - x - 2

b2 = Bisection(g, 1, 2)
akar2 = b2.solve()

b2.print_table()
print("Akar:", akar2)
b2.plot()