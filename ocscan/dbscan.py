import pandas as pd
import numpy as np
from sklearn.cluster import DBSCAN
from sklearn.preprocessing import StandardScaler
# general packages

import ocscan.download
import ocscan.plot
import ocscan.save
import ocscan.show
# my modules


	
def dbscan(data, N, eps, input=False):
	"""Searching for clusters in data on the basis of DBSCAN algorithm and Principal Component Analysis in 4D hyper-sphere"""
	names=['pmRA','pmDE','RA_ICRS','DE_ICRS'] 
	N_dim = len(names)				  # dimensions. 					  
									  # physical 4D-space
	mask = np.array([True for i in range(len(data))])
	for x in names:
		mask = mask & data[x].notna()   # deleting empty data lines (table strings)

	Data = data[mask]   
	NormMainData = StandardScaler().fit_transform(Data[names])
	db = DBSCAN(eps, N).fit(NormMainData)
	Data['labels'] = db.labels_
	core_samples_mask = np.zeros_like(db.labels_, dtype=bool)
	core_samples_mask[db.core_sample_indices_] = True
	
	return Data, db.labels_, core_samples_mask
	
