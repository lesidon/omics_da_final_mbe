import numpy as np
import pandas as pd
import scipy
import cooler


resol=100000
c=cooler.Cooler('/gss/home/l.sidorov/omics_final_project/GSE168524_neurons_fem_wt_allValidPairs.mcool::resolutions/%s'%resol)

pix=c.pixels(join=True)[:]

pix.chrom1=pix.chrom1.astype(str)
pix.chrom2=pix.chrom2.astype(str)


pix1=pix.groupby(['chrom1','start1']).sum().reset_index()[['chrom1','start1','count']]
pix=pix.loc[~((pix.chrom1==pix.chrom2)&(pix.start1==pix.start2))]

pix=pix.groupby(['chrom2','start2']).sum().reset_index()[['chrom2','start2','count']]
pix1.columns=[0,1,2]
pix.columns=[0,1,2]


pix=pd.concat([pix1,pix])

pix1=None

pix=pix.groupby([0,1]).sum().reset_index()

pix['lab']=pix[0].astype(str)+':'+pix[1].astype(str)

chr_size=pd.read_csv('chrsizes.csv',sep='\t',index_col=0)

bins=cooler.binnify(chr_size['size'],resol)
bins.chrom=bins.chrom.astype(str)

bins['lab']=bins.chrom.astype(str)+':'+bins.start.astype(str)
bins.index=bins.lab

bins['count']=0
bins.loc[list(pix.lab),'count']=list(pix[2])

bins['x1']=0
bins['x2']=1

pix=None

fragments=bins[['chrom','x1','start','count','x2']]
fragments.sort_values(['chrom','start'],inplace=True)
fragments.to_csv('./fithic_inputs/fragments.gzip',sep='\t',header=None,index=None,compression='gzip')

pix=c.pixels(join=True)[:]
interactions=pix[['chrom1','start1','chrom2','start2','count']]
interactions.to_csv('./fithic_inputs/interactions.txt.gzip',sep='\t',header=None,index=None,compression='gzip')


