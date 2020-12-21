import numpy as np

def results(Data, labels, core_samples_mask):    
    """Save results into .csv file"""
    Data[(labels == 0) & core_samples_mask].to_csv('res-centers.csv',index=False, mode = 'w')
    Data[(labels == 0) & ~core_samples_mask].to_csv('res-neighbours.csv',index=False, mode = 'w')
    Data[(labels == 0)].to_csv('res-cluster.csv',index=False, mode = 'w')

