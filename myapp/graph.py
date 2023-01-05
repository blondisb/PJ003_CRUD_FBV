#%%
import matplotlib.pyplot as plt
import numpy as np
from io import StringIO

def make_graph():
    x = np.arange(0, np.pi*3, .1)
    y = np.sin(x)

    fig = plt.figure()
    # fig.show()
    plt.plot(x,y)

    imgdata = StringIO()
    fig.savefig(imgdata, format='svg')
    imgdata.seek(0)

    data = imgdata.getvalue()
    return data

# make_graph()