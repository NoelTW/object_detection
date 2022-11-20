import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import patches



class MyDataFrame(pd.DataFrame):
    
    def __init__(self,dataset):
        """
        """
        super(MyDataFrame, self).__init__(dataset)
    
    @property
    def _constructor(self):
        if MyDataFrame.columns == ['image_id', 'x_min', 'y_min', 'x_max', 'y_max', 'frame', 'isNight','label']:
            return MyDataFrame
        else:
            print('This is not valid')

    def image2Array(self,idx):
        return plt.imread(self.iloc[idx].image_id)
    
    def get_label(self,idx):
        return self.iloc[idx].label

    def getObjectCoordination(self,idx):
        x_min = self.iloc[idx].x_min
        x_max = self.iloc[idx].x_max
        y_min = self.iloc[idx].y_min
        y_max = self.iloc[idx].y_max
        return x_min,y_min,x_max-x_min,y_max-y_min

    def showImage(self,idx,*args,**kargs):
        _, ax = plt.subplots(*args,**kargs)
        img = self.image2Array(idx)
        ax.imshow(img)
        ax.grid(False)
        plt.show()

    def plotDetection(self,idx,*args,**kargs):
        x_min,y_min,width,height = self.getObjectCoordination(idx)
        img = self.image2Array(idx)
        _, ax = plt.subplots(*args,**kargs)  
        rect = patches.Rectangle(
        (x_min, y_min),
        height=height,
        width=width,
        linewidth=1,
        edgecolor='r',
        facecolor='none'
        )
        ax.imshow(img)
        ax.add_patch(rect)
        ax.grid(False)
        plt.title(self.get_label(idx))
        plt.show()