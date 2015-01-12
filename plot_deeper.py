import pandas as pd
import numpy as np
import matplotlib.pylab as plt
import matplotlib.mlab as m

train_sub=[2,6,7]
train_sub_higher=[11,12,13]
train_sub_higher2= [14,16,17]
train_sub_higher3=[18,20,21,22,23,24,26]
header_list = ['C5','C3','C1','Cz','C2','C4','C6','CP5','CP3','CP1','CPz','CP2','CP4','CP6','P5','P3','P1','Pz','P2','P4','P6','POz','O1','O2']
for i in train_sub_higher3:
    j=1
    while j<6:
        df = pd.read_csv("../train/Data_S"+str(i)+"_Sess0"+str(j)+".csv")
        k=0
        for k in range(len(header_list)):
            column=df[header_list[k]]
            plt.figure()
            plt.psd(column,NFFT=256, Fs=200)
            plt.title('Subject-'+str(i)+', Session '+str(j)+'-'+' '+header_list[k])
            plt.savefig('../CPlobes-plots/'+header_list[k]+'Sb'+str(i)+'ss'+str(j))
            plt.close()
        j=j+1
            
    
    
    
