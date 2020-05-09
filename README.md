# Fourier Draw Animation

Simple Python project to draw any continuous shape using Fourier series.

# Install requirements & Start

```
pip3 install numpy matplotlib svgpathtools
python3 main.py
```

# Sample Code

```python
from SVGReader import SVGReader
from Fourier import Fourier
from FourierPlot import FourierPlot

data = SVGReader("pi.svg")
coef = Fourier(data, N=40).sample()
plot = FourierPlot(coef, frames=200, interval=40)
plot.plot()
```

# Credit

Icon made by [Stephen Hutchings](https://www.flaticon.com/authors/stephen-hutchings)
