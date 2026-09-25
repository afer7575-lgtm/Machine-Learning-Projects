import matplotlib.pyplot as plt
from pathlib import Path

class Visualization:
    def __init__(self,df, path_to_save, not_us = []):
        self.df = df
        self.path_to_save = path_to_save
        self.not_us = not_us

    def visual(self, name_x, names_y=None, name_mark = False, not_lin=False):
        if not(names_y):
            names_y = self.df.columns.drop([name_x] + self.not_us).tolist()
        if isinstance(names_y,str): names_y = [names_y]
        for name_y in names_y:
            plt.figure(figsize=(12, 4))
            x = self.df[name_x]
            y = self.df[name_y]

            if not_lin:
                plt.scatter(x,y)
            else:
                plt.plot(x,y)

            if name_mark:
                x_m = self.df[self.df[name_mark]==True][name_x]
                y_m = self.df[self.df[name_mark] == True][name_y]
                plt.scatter(x_m, y_m, color="red")
            plt.xticks([])
            plt.xlabel(name_x)
            plt.ylabel(name_y)

            image_path = self.path_to_save / f"{name_y}_image.png"

            plt.savefig(image_path)
            plt.close()