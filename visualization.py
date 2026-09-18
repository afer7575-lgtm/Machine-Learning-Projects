import matplotlib.pyplot as plt

class Visualizaton:
    def __init__(self,df):
        self.df = df

    def visual(self, name_x, name_y):
        name_x = "timestamp"
        name_y = "temperature"
        x = self.df[name_x]
        y = self.df[name_y]

        plt.scatter(x,y)
        plt.xticks([])
        plt.xlabel(name_x)
        plt.ylabel(name_y)

        plt.savefig(f"{name_y}_image.png")
        plt.close()