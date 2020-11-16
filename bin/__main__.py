import bin.download
import bin.plotgraphs
# my modules

from sklearn.cluster import DBSCAN
from sklearn.decomposition import PCA
import pandas as pd
import numpy as np
import argparse as ap
# general packages

def main():
	"""Searching for clusters in data on the basis of DBSCAN algorithm and Principal Component Analysis in 4D hyper-sphere"""
	parser=ap.ArgumentParser(description = 'Searching for clusters in data on the basis of DBSCAN algorithm and Principal Component Analysis in 4-dimensional space')
	parser.add_argument('-N', default = 30)
	parser.add_argument('-eps', default = 0.3)
	parser.add_argument('-ra', default = 124.90)
	parser.add_argument('-de', default = -38.27)
	p=parser.parse_args()	
	Eps_DBSCAN=float(p.eps)
	N_DBSCAN=float(p.N)
	ra_download=float(p.ra)
	de_download=float(p.de)

	bin.download.gaiadata(ra_download, de_download) # ra,dec,radius in degrees (radius_default = 0.0833 -> 5 arcmin)
									  # download data from gaia dr2
	data = pd.read_csv('data.csv', delimiter=',')

	N_dim = 4                         # dimensions. 
									  # WARNING: 
									  # DON'T CHANGE IT without adding fifth column in names ('plx')
	names=['pmRA','pmDE','RA_ICRS','DE_ICRS'] 
									  # physical 4D-space
	mask=np.array([True for i in range(len(data))])
	for x in names:
		mask=mask & data[x].notna()   # deleting empty data lines (table strings)

	Data=data[mask]    
	sigs = list(np.sqrt(Data[names].var()))
	NormMainData = np.true_divide(Data[names], sigs)
	pca = PCA(n_components=N_dim)
	X = pca.fit_transform(NormMainData)
									  # Principal Component Analysis

	db = DBSCAN(eps = Eps_DBSCAN, min_samples = N_DBSCAN).fit(X)
	core_samples_mask = np.zeros_like(db.labels_, dtype=bool)
	core_samples_mask[db.core_sample_indices_] = True
	labels = db.labels_
	n_clusters_ = len(set(labels)) - (1 if -1 in labels else 0)
	n_noise_ = list(labels).count(-1)
	print('Estimated number of clusters: %d' % (n_clusters_))
	unique_labels = set(labels)
									  # DBSCAN - clustering                                 
	limits_pmra_pmde = [[-10, 5],[-5, 10]]        # pmra_min, pmra_max, pmde_min, pmde_max
	limits_ra_de = [[min(Data['RA_ICRS']),max(Data['RA_ICRS'])],[min(Data['DE_ICRS']),max(Data['DE_ICRS'])]]
												  # CAN CHANGE IT FOR YOUR SKY FIELD
	bin.plotgraphs.graphs(Data, unique_labels, labels, core_samples_mask, limits_ra_de, limits_pmra_pmde)
	return n_clusters_
if __name__ == '__main__':				 
    main()
	