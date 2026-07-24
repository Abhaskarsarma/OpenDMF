from visualization.renderer import Renderer

import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib.patches import Rectangle
from matplotlib.patches import Circle

class MatplotlibRenderer(Renderer):

    def __init__(self):
        self.fig = None
        self.ax = None

    def render(self, history):     
        self.fig, self.ax = plt.subplots(figsize=(7,7))
        self.ax.set_aspect("equal")
        self.history = history
        ani = animation.FuncAnimation(
        self.fig,
        self.update,
        frames=len(history),
        interval=300,
        repeat=False
        )

        plt.show()
        pass
        
    def draw_grid(self, snapshot):
        rows = len(snapshot.grid)
        cols = len(snapshot.grid[0])
        self.ax.clear()
        self.ax.set_xlim(0, cols)
        self.ax.set_ylim(0, rows)
        self.ax.set_xticks(range(cols+1))
        self.ax.set_yticks(range(rows+1))
        self.ax.grid(True)
        self.ax.invert_yaxis()
        self.ax.set_title("OpenDMF Simulation")
        self.ax.set_xlabel("Column")
        self.ax.set_ylabel("Row")
        
        for r,row in enumerate(snapshot.grid):
            for c,cell in enumerate(row):
                if cell.blocked:
                    rect = Rectangle((c,r),1,1,color="black")
                    self.ax.add_patch(rect)
                elif cell.droplet is not None:
                    circle = Circle((c+0.5,r+0.5),0.35,color="blue")
                    self.ax.add_patch(circle)
                    
    def update(self, frame):
        snapshot = self.history[frame]
        self.draw_grid(snapshot)