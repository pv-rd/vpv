import Errors as e

L = e.Data()
f = e.Data()

file_name = "1.txt"

L.read(file_name=file_name, e = 0.05, sep_dec=',')
f.read(file_name=file_name, col=1, e = 0.1, sep_dec=',')

y = [1/(x*x) for x in f.v]
ey = [2*(f.e[i]/f.v[i])*y[i] for i in range(len(y))]
Y = e.Data(y, ey)

X = e.Data([(x - 13.15) * 0.001 for x in L.v], [x*0.001*2 for x in L.e])


P = e.Plot(X, Y, "L, м", "$f^{-2}$, Гц$^{-2}$")

K, B = P.draw()

print(f"A = ({K})")
print(f"delta = ({B/K})")
