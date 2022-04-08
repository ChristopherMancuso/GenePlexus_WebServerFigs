import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('main_result.tsv',sep='\t')
print(df.shape)
df = df[df['Score Type']=='auPRC']
df = df[~(df['Network']=='InBioMap')]
print(df.shape)
df = df[df['Validation Split']=='Holdout']
print(df.shape)
df = df[df['Method'].isin(['SL-A','SL-I','SL-E'])]
print(df.shape)
print(df.head())
df_GO = df[df['Geneset Collection']=='GOBP']
print(df_GO.shape)
df_Dis = df[df['Geneset Collection']=='DisGeNet']
print(df_Dis.shape)

fig, axs = plt.subplots(1,2,figsize=(8,4))
sns.boxplot(data=df_GO,y='Score',x='Network',hue='Method',
             showfliers=False,notch=True,ax=axs[0])
sns.boxplot(data=df_Dis,y='Score',x='Network',hue='Method',
             showfliers=False,notch=True,ax=axs[1])


axs[0].set_ylabel('log2(auPRC/prior)')
axs[1].set_ylabel('')
axs[0].set_xlabel('')
axs[1].set_xlabel('')

axs[0].set_title('Gene Ontology Biological Processes')
axs[1].set_title('DisGeNet')

fig.subplots_adjust(top=0.9,bottom=0.1,left=0.06,right=0.98)
fig.savefig('WebServer_ModelComparison.png',dpi=400)

plt.show()