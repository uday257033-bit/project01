import seaborn as sns 
import matplotlib.pyplot as plt
import numpy as np

data=[11,14,33,44,55,67,11,23,34,65,64,44,44,65,56,12,23,43,69,1,2,34,45]
plot=['histogram','KERNAL_DENSITY']
for plots in plot:
    if plots =='Histogram':
        sns.histplot(data)
        plt.title("Histogram chart")
        plt.show()
    elif plots =='KERNAL_DENSITY':
        sns.kdeplot(data)
        plt.title("KERNAL_DENSITY")
        plt.show()

data=[11,14,33,44,55,67,11,23,34,65,64,44,44,65,56,12,23,43,69,1,2,34,45]
plot=['histogram','KERNAL_DENSITY']
for plots in plot:
    if plots =='Histogram':
        sns.histplot(data)
        plt.title("Histogram chart")
        plt.show()
    elif plots =='KERNAL_DENSITY':
        sns.kdeplot(data)
        plt.title("KERNAL_DENSITY")
        plt.show()
data1=[11,14,33,44,55,67,11,23,34,65,64,44,44,65,56,12,23,43,69,1,2,34,45]
data2=[11,14,3,14,25,67,31,23,64,65,64,84,44,65,56,0,23,43,69,1,2,34,45]
data3=[11,14,3,4,5,67,31,3,64,5,4,84,44,65,56,0,23,43,69,1,2,34,45]
group=[data1,data2,data3]
sns.violinplot(data=group)
plt.title("example of violin plot")
plt.show()
