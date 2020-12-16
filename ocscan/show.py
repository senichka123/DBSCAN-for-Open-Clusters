import numpy as np

def NumberOfClusters(labels): 	
    """Show results of clustering for DBSCAN"""
    n_clusters_ = len(set(labels)) - (1 if -1 in labels else 0)
    print('Estimated number of clusters: %d' % (n_clusters_))
    return n_clusters_
									 

