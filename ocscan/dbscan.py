import pandas as pd
import numpy as np
from sklearn.cluster import DBSCAN
from sklearn.decomposition import PCA
# general packages

import ocscan.download
import ocscan.plot
import ocscan.save
import ocscan.show
# my modules


	
def dbscan(N, eps, ra, de, plot=False, save=False):
	"""Searching for clusters in data on the basis of DBSCAN algorithm and Principal Component Analysis in 4D hyper-sphere"""
	data = ocscan.download.gaiadata(ra, de) # ra,dec,radius in degrees (radius_default = 0.0833 -> 5 arcmin)
									  # download data from gaia dr2
	names=['pmRA','pmDE','RA_ICRS','DE_ICRS'] 
	N_dim = len(names)				  # dimensions. 					  
									  # physical 4D-space
	mask=np.array([True for i in range(len(data))])
	for x in names:
		mask=mask & data[x].notna()   # deleting empty data lines (table strings)

	Data=data[mask]    
	NormMainData = np.true_divide(Data[names], list(Data[names].std()))
	db = DBSCAN(eps, N).fit(NormMainData)
	Data['labels']=db.labels_
	core_samples_mask = np.zeros_like(db.labels_, dtype=bool)
	core_samples_mask[db.core_sample_indices_] = True
	
	if plot:
		ocscan.plot.graphs(Data, db.labels_, core_samples_mask)
	if save:
		ocscan.save.results(Data, db.labels_, core_samples_mask)
		
	return db.labels_
	
