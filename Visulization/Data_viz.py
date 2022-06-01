#import libraries

import seaborn as sns
import matplotlib.pyplot as plt

#import theme
sns.set_theme(style="ticks", color_codes= True)

#import data set

kashti = sns.load_dataset("titanic")
# print(kashti)

#plot basic graph with 1 variable (count)
p = sns.countplot(x = "sex", data= kashti)
plt.show()

#plot basic graph with 2 variable (count plot)

p = sns.countplot(x = "sex", hue= "class", data= kashti)
plt.show()

#plot basic graph with 2 variable (count plot) with title
p = sns.countplot(x = "sex", hue= "class", data= kashti)
p.set_title("kashti count plot")
plt.show()