import matplotlib.pyplot as plt
from pathlib import Path

class Visualization:
    def __init__(self,df, path_to_save):
        self.df = df
        self.path_to_save = path_to_save

    def visual(self, name_x, name_y):
        plt.figure(figsize=(12, 4))
        x = self.df[name_x]
        y = self.df[name_y]

        plt.plot(x,y)
        plt.xticks([])
        plt.xlabel(name_x)
        plt.ylabel(name_y)

        image_path = self.path_to_save / f"{name_y}_image.png"

        plt.savefig(image_path)
        plt.close()

    def visual_all(self, name_x):
        for name_y in self.df.columns.drop(name_x).tolist(): self.visual(name_x, name_y)

    #По-хорошему надо нахер убрать visual_all и сделать так чтобы visual работал с несколькими значениями name_y
    #и перебирал columns при отсутствии name_y