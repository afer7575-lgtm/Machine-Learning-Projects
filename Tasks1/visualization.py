import matplotlib.pyplot as plt
from pathlib import Path

class Visualizaton:
    def __init__(self,df):
        self.df = df

    def visual(self, name_x, name_y):
        x = self.df[name_x]
        y = self.df[name_y]

        plt.scatter(x,y)
        plt.xticks([])
        plt.xlabel(name_x)
        plt.ylabel(name_y)

        image_path = Path(__file__).parent / f"{name_y}_image.png"
        plt.savefig(image_path)
        plt.close()