import pandas as pd
import numpy as np
import matplotlib.pylab as plt
import matplotlib.mlab as m

df = pd.read_csv("../train/Data_S02_Sess05.csv")
header_list = df.columns.values.tolist()
i=1
for i in range(len(header_list)-1):
    column=df[header_list[i]]
    plt.figure()
    plt.psd(column,NFFT=256, Fs=200)
    plt.title('Subject-2, Session 5 -'+' '+header_list[i])
    plt.savefig('../Plots/Subject-2-session-5/Sb2ss5'+header_list[i])
    plt.close()
#time= df['Time']
#plt.figure()
#plt.psd(normlized2,NFFT=256, Fs=rate)
#plt.show()
