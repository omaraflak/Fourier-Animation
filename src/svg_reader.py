import numpy as np
from svgpathtools import svg2paths

class SVGReader():
    def __init__(self, filepath):
        paths, _ = svg2paths(filepath)
        self.points = paths[0].point

    def get(self, index):
        return np.conj(self.points(index))
