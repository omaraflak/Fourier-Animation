import numpy as np
from matplotlib import pyplot as plt
from matplotlib import animation

class FourierPlot():
    lines = None
    
    def __init__(self, coef, frames, interval, exclude_static_component=True):
        self.coef = coef
        self.frames = frames
        self.interval = interval
        self.exclude_static_component = exclude_static_component
        self.fig = None

    @staticmethod
    def init():
        for line in FourierPlot.lines:
            line.set_data([], [])
            line.set_color((0, 0, 0, 0.5))
        FourierPlot.lines[len(FourierPlot.lines) - 1].set_data([], [])
        FourierPlot.lines[len(FourierPlot.lines) - 1].set_color((0.1, 0.5, 0.7, 0.8))
        return FourierPlot.lines

    @staticmethod
    def animate(i, self):
        center = 0+0j
        for idx, item in enumerate(self.coef):
            n, c = item['n'], item['c']
            f = lambda t : c * np.exp(2*np.pi*n*t*1j)
            tip = f((i+1)/self.frames) + center
            if self.exclude_static_component:
                if idx > 0:
                    FourierPlot.lines[idx - 1].set_data([center.real, tip.real], [center.imag, tip.imag])
            else:
                FourierPlot.lines[idx].set_data([center.real, tip.real], [center.imag, tip.imag])
            center = tip
        pencil = FourierPlot.lines[len(FourierPlot.lines) - 1]
        pencil.set_xdata(np.append(pencil.get_xdata(), [center.real]))
        pencil.set_ydata(np.append(pencil.get_ydata(), [center.imag]))
        return FourierPlot.lines

    def get_lim(self):
        points = [np.sum([item['c']*np.exp(2*np.pi*item['n']*t*1j) for item in self.coef]) for t in np.arange(0, 1, 0.01)]
        center = np.average(points)
        diff = np.max(np.absolute(points - center)) + 1
        xcenter, ycenter = center.real, center.imag
        return ((xcenter-diff, xcenter+diff), (ycenter-diff, ycenter+diff))

    def plot(self, size=(8, 8), filename=None):
        fig = plt.figure(figsize=size)
        xlim, ylim = self.get_lim()
        ax = plt.axes(xlim=xlim, ylim=ylim)
        ax.set_aspect("equal")
        FourierPlot.lines = [ax.plot([], [])[0] for i in range(len(self.coef) - int(self.exclude_static_component))]
        FourierPlot.lines.append(ax.plot([], [])[0])

        anim = animation.FuncAnimation(
            fig, FourierPlot.animate,
            fargs=(self,), init_func=FourierPlot.init,
            frames=self.frames, interval=self.interval,
            blit=True, repeat=True
        )
        if filename:
            anim.save(filename, fps=30, extra_args=['-vcodec', 'libx264'])

        plt.show()
        return fig
