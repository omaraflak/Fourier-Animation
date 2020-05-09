from src import SVGReader, Fourier, FourierPlot

print("read svg...")
data = SVGReader("svg/twitter.svg")
print("compute fourier coef...")
coef = Fourier(data, N=100).sample()
print("plot...")
plot = FourierPlot(coef, frames=300, interval=20)
plot.plot()
