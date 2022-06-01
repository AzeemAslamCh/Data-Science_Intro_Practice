#import library

# from tokenize import PlainToken
# from tracemalloc import Snapshot
from matplotlib import pyplot
import pandas as pd

#import data from file
chilla = pd.read_csv("data_viz.csv")
import seaborn as sns
import matplotlib.pyplot as plt 
sns.set_theme(style="ticks", color_codes=True)
p= sns.countplot(x="Gender", hue="Location", data=chilla)
plt.show()