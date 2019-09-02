from SVGReader import SVGReader
from Fourier import Fourier
from FourierPlot import FourierPlot

print("read svg...")
data = SVGReader("twitter.svg").data()
print("compute fourier coef...")
coef = Fourier(data, N=100).sample()
print("plot...")
plot = FourierPlot(coef, frames=300, interval=20)
plot.plot()