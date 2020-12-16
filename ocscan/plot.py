import matplotlib.pyplot as plt
import numpy as np
from matplotlib import cm



def graphs(Data, labels, core_samples_mask):
    """Plot 4 main graphs for DBSCAN - data
    Plx - Gmag
    RA - DEC
    pmRA - pmDE
    BP-RP - Gmag
    """
    unique_labels = set(labels)
    plt.rcParams["figure.figsize"] = (5, 5)
    colors = [plt.cm.Spectral(each)
              for each in np.linspace(0.5, 1, len(unique_labels))]
    
    fig1 = plt.figure(1)
    plt.clf()
    for k, col in zip(unique_labels, colors):
        
        if k == -1:
            continue
        class_member_mask = (labels == k)
        xy = Data[class_member_mask & core_samples_mask]
        plt.plot(xy.Plx, xy.pmRA, 'o', markerfacecolor=tuple(col),
                 markeredgecolor='k', markersize=9)
        if k==-1:
            xy = Data[class_member_mask & ~core_samples_mask]
            plt.plot(xy.Plx, xy.pmRA, 'o', markerfacecolor=tuple(col),
               markeredgecolor='b', markersize=1, alpha=0.5)
        else:
            xy = Data[class_member_mask & ~core_samples_mask]
            plt.plot(xy.Plx, xy.pmRA, 'o', markerfacecolor=tuple(col),
               markeredgecolor='k', markersize=5)
        
    plt.gca().invert_yaxis()
    plt.title('Plx-pmRA')
    plt.xlabel('parallax')
    plt.ylabel('pmRA')
    x1,x2=plt.gca().get_xlim()
    plt.show()
    
    
    
    fig6 = plt.figure(2)
    plt.clf()
    for k, col in zip(unique_labels, colors):
        class_member_mask = (labels == k)
        xy = Data[class_member_mask & core_samples_mask]
        plt.plot(xy.RA_ICRS, xy.DE_ICRS, 'o', markerfacecolor=tuple(col),
                 markeredgecolor='k', markersize=9)
        if k==-1:
            xy = Data[class_member_mask & ~core_samples_mask]
            plt.plot(xy.RA_ICRS, xy.DE_ICRS, 'o', markerfacecolor=tuple(col),
                     markeredgecolor='b', markersize=1, alpha=0.1)
        else:
            xy = Data[class_member_mask & ~core_samples_mask]
            plt.plot(xy.RA_ICRS, xy.DE_ICRS, 'o', markerfacecolor=tuple(col),
                     markeredgecolor='k', markersize=5)
    
    plt.title('RA-DEC')
    plt.xlabel('RA')
    plt.ylabel('DEC')
    plt.show()
    
    
    
    fig2 = plt.figure(3)
    plt.clf()
    for k, col in zip(unique_labels, colors):
        class_member_mask = (labels == k)
        if k==-1:
            xy = Data[class_member_mask & ~core_samples_mask]
            plt.plot(xy.pmRA, xy.pmDE, 'o', markerfacecolor=tuple(col),
                     markeredgecolor='b', markersize=1, alpha=0.1)
        else:
            xy = Data[class_member_mask & ~core_samples_mask]
            plt.plot(xy.pmRA, xy.pmDE, 'o', markerfacecolor=tuple(col),
                         markeredgecolor='k', markersize=5)
        xy = Data[class_member_mask & core_samples_mask]
        plt.plot(xy.pmRA, xy.pmDE, 'o', markerfacecolor=tuple(col),
                     markeredgecolor='k', markersize=9, alpha=1)
    
    plt.title('Proper Motion')
    plt.xlim([-20,10])
    plt.ylim([-10,20])
    plt.xlabel('pmra')
    plt.ylabel('pmdec')
    plt.show()
    
    
    
    fig5 = plt.figure(4)
    plt.clf()
    for k, col in zip(unique_labels, colors):
        if k == -1:
            continue
        class_member_mask = (labels == k)
        
        xy = Data[class_member_mask & core_samples_mask]
        plt.plot(xy.BP_RP, xy.Gmag, 'o', markerfacecolor=tuple(col),
                     markeredgecolor='k', markersize=9)
        xy = Data[class_member_mask & ~core_samples_mask]
        plt.plot(xy.BP_RP, xy.Gmag, 'o', markerfacecolor=tuple(col),
                 markeredgecolor='k', markersize=5)
    
    plt.title('Color-mag')
    plt.xlabel('bp-rp')
    plt.ylabel('Gmag')
    y1,y2=plt.gca().get_ylim()
    x1,x2=plt.gca().get_xlim()
    plt.gca().invert_yaxis()
    plt.show()
    
    
    Data['labels']=labels
    Data[class_member_mask & core_samples_mask].to_csv('res-centers.csv',index=False, mode = 'w')
    Data[class_member_mask & ~core_samples_mask].to_csv('res-neighbours.csv',index=False, mode = 'w')
    Data[class_member_mask].to_csv('res-cluster.csv',index=False, mode = 'w')

graphs.__doc__ = """Ploting results (only graphs) + saving results (into .csv files)"""
