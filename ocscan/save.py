import numpy as np

def results(Data, labels, core_samples_mask):   
    """Save results into .csv file"""
    unique_labels = set(labels)
    for k in unique_labels:
        if k == -1:
            continue
        class_member_mask = (labels == k)
        
    Data[class_member_mask & core_samples_mask].to_csv('res-centers.csv',index=False, mode = 'w')
    Data[class_member_mask & ~core_samples_mask].to_csv('res-neighbours.csv',index=False, mode = 'w')
    Data[class_member_mask].to_csv('res-cluster.csv',index=False, mode = 'w')

