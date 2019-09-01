from SVGReader import SVGReader
from Fourier import Fourier
from FourierPlot import FourierPlot

print("read svg...")
data = SVGReader("pi.svg").data()
print("compute fourier coef...")
coef = Fourier(data, N=40).sample()
print("plot...")
plot = FourierPlot(coef, frames=200, interval=40)
plot.plot()