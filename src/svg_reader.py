import numpy as np
from svgpathtools import svg2paths

class SVGReader():
    def __init__(self, filepath):
        self.filepath = filepath
        self.points = []

    def data(self):
        paths, _ = svg2paths(self.filepath)
        self.points = paths[0].point
        return self

    def get(self, index):
        return np.conj(self.points(index))