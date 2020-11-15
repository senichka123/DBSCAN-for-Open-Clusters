import download
import plotgraphs
# my modules

from sklearn.cluster import DBSCAN
from sklearn.decomposition import PCA
import pandas as pd
import numpy as np

import pytest
# general packages

def main(N_DBSCAN,Eps_DBSCAN):
    
    """Searching for clusters in data on the basis of DBSCAN algorithm
    and Principal Component Analysis in 4D hyper-sphere"""
    
    download.gaiadata(124.90, -38.27) # ra,dec,radius in degrees (radius_default = 0.0833 -> 5 arcmin)
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
    limits_ra_de = [[124.85,124.95],[-38.3,-38.24]] # ra_min, ra_max, de_min, de_max
    limits_pmra_pmde = [[-4, -1.5],[1, 5.5]]        # pmra_min, pmra_max, pmde_min, pmde_max
    ## limits_ra_de = [[min(Data['RA_ICRS']),max(Data['RA_ICRS'])],[min(Data['DE_ICRS']),max(Data['DE_ICRS'])]]
    ## limits_pmra_pmde = [[min(Data['pmRA']),max(Data['pmRA'])],[min(Data['pmDE']),max(Data['pmDE'])]]
                                                    # CAN CHANGE IT FOR YOUR SKY FIELD
                                                    #  DELETE '##' for default (all data)
    plotgraphs.graphs(Data, unique_labels, labels, core_samples_mask, limits_ra_de, limits_pmra_pmde) 
                                      #ploting module 
    

    
if __name__ == '__main__':
    main(30, 0.3) # Number of neighbours, epsilon - radius of hyper-sphere
                  # CAN VARY FOR ANOTHER SKY FIELD
                  # BEST PARAMETER FIT DOESN'T INCLUDE IN THIS WORK...
                  # USING 30, 0.3 - the best way for finding some OPEN CLUSTER in MIDDLE DENSITY SKY FIELD
    ?download.gaiadata
    #?main
    #?plotgraphs.graphs



