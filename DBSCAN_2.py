from sklearn.cluster import DBSCAN
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA
import numpy as np
import math
import argparse as ap
import random
from matplotlib import colors as mcolors
import pyperclip

from sklearn.neighbors import KernelDensity
from sklearn.model_selection import GridSearchCV
from scipy.optimize import curve_fit
import os

from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm


parser=ap.ArgumentParser(description = '''Searching for clusters in data on the basis
                         of DBSCAN algorithm and Principal Component Analysis either in
                         5 or 4-dimensional space''')

#parser.add_argument('input_data', help = '''Name of the CSV file with input data. The file must 
#                    contain the folowing columns: l - galactic longitude [deg], b - 
#                    galactic latitude [deg], dist - distance[pc], pmra [mas/yr], pmdec [mas/yr]''')
#parser.add_argument('N_DBSCAN', help = 'Number of neighbours for DBSCAN', type=int)
#parser.add_argument('Eps_DBSCAN', help = 'DBSCAN epsilon parameter', type=float)
parser.add_argument('-d', '--distance', action='store_true',
                    help = 'use distanse as the 5th patameter')
parser.add_argument('-p', '--plot', action='store_true',
                    help = 'plot graphs')
parser.add_argument('-o', '--output', nargs='?', default = True, metavar = 'NAME',
                    help = '''Name of the ouput CSV file. Default is "clusters_out.csv". 
                    If missed, the output file will not be created.''')
plt.rcParams["figure.figsize"] = (5, 5)
args=parser.parse_args()
name1=int(1754)
args.input_data=str(name1)+'S.csv'
args.N_DBSCAN=30
args.Eps_DBSCAN=0.3
data = pd.read_csv(args.input_data, delimiter=',')
if args.distance:
    #main_data = data[['pmRA','pmDE','RA_ICRS','DE_ICRS', 'Plx']]
    #dop_data = data[['BPmag','BP_RP', 'Plx', 'Gmag']]
    N_dim = 5
    print('5-dimensional')
else:
    #main_data = data[['pmRA','pmDE','RA_ICRS','DE_ICRS']]
    #dop_data = data[['BPmag','BP_RP','RA_ICRS','Plx','Gmag']]
    N_dim = 4
    print('4-dimensional')
    
names=['pmRA','pmDE','RA_ICRS','DE_ICRS']
#names=['pmRA','pmDE','RA_ICRS','DE_ICRS','Plx'] #5D

mask=np.array([True for i in range(len(data))])
for x in names:
    mask=mask & data[x].notna()

Data=data[mask]
#print(Data)
    
sigs = list(np.sqrt(Data[names].var()))
#print(sigs)
NormMainData = np.true_divide(Data[names], sigs)
pca = PCA(n_components=N_dim)
X = pca.fit_transform(NormMainData)

db = DBSCAN(eps = args.Eps_DBSCAN, min_samples = args.N_DBSCAN).fit(X)
core_samples_mask = np.zeros_like(db.labels_, dtype=bool)
core_samples_mask[db.core_sample_indices_] = True
labels = db.labels_
n_clusters_ = len(set(labels)) - (1 if -1 in labels else 0)
n_noise_ = list(labels).count(-1)
print('Estimated number of clusters: %d' % (n_clusters_))
#unique_labels = set(labels)
#print(len(labels))
#print(unique_labels)
'''
for k in unique_labels:
    if k == -1:
        continue
    class_member_mask = (labels == k)
    xy = Data[class_member_mask, Gmag < 19]
    
print(xy.Gmag)
a = np.asarray(xy.Gmag)
print(a)
for z in range(len(labels)):
    if labels[z]==0:
        labels[z]=1
'''
unique_labels = set(labels)

if args.plot:
    colors = [plt.cm.Spectral(each)
              for each in np.linspace(0.5, 1, len(unique_labels))]
    
    fig1 = plt.figure(1)
    plt.clf()
    for k, col in zip(unique_labels, colors):
        
        if k == -1:
            continue
        #if k == 0:
        #    continue
    
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
    #plt.xlim([-0.5,1.1])
    plt.show()
    
    #print(xy)
    '''
    
    fig4 = plt.figure(4)
    plt.clf()
    for k, col in zip(unique_labels, colors):
        if k == -1:
            continue
       # if k == 0:
       #     continue
        
        class_member_mask = (labels == k)
        xy = main_data[class_member_mask & core_samples_mask]
        plt.plot(xy.par, xy.l, 'o', markerfacecolor=tuple(col),
                 markeredgecolor='k', markersize=9)
    
        xy = main_data[class_member_mask & ~core_samples_mask]
        plt.plot(xy.par, xy.l, 'o', markerfacecolor=tuple(col),
               markeredgecolor='k', markersize=5)
    
    plt.title('parallax-l')
    plt.xlabel('parallax')
    plt.ylabel('l')
    y1,y2=plt.gca().get_ylim()
    x1,x2=plt.gca().get_xlim()
    plt.show(1)
    
    '''
    
    
    
    
    
    
    fig6 = plt.figure(6)
    plt.clf()
    for k, col in zip(unique_labels, colors):
       # if k == -1:
       #     continue
       # if k == 0:
       #     continue
    
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
    #ax.invert_xaxis()
   # plt.xlim([124.87,124.925])
   # plt.ylim([-38.29,-38.25])
   # plt.xlim([212.85,212.95])
   # plt.ylim([-61.72,-61.68])
    #plt.axis('square')
    plt.show()
    
    
    #print(unique_labels, colors)
    
    fig2 = plt.figure(2)
    plt.clf()
    for k, col in zip(unique_labels, colors):
       # if k == -1:
       #     continue
       # if k == 0:
       #     continue
        
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
    
    #x1=xy.pmRA.min()
    #x2=xy.pmRA.max()
    #y1=xy.pmDE.min()
    #y2=xy.pmDE.max()
    plt.title('Proper Motion')
    plt.xlim([-7,2])
    plt.ylim([-3,8])
    plt.xlabel('pmra')
    plt.ylabel('pmdec')
   # plt.axis('square')
    plt.show(2)
    
    '''
    fig7 = plt.figure(7)
    plt.clf()
    for k, col in zip(unique_labels, colors):
        if k == -1:
            continue
        if k == 0:
            continue
        
        class_member_mask = (labels == k)
        
        xy = Data[class_member_mask & core_samples_mask]
        plt.plot(xy.pmRA, xy.pmDE, 'o', markerfacecolor=tuple(col),
                     markeredgecolor='k', markersize=9)
        
        xy = Data[class_member_mask & ~core_samples_mask]
        plt.plot(xy.pmRA, xy.pmDE, 'o', markerfacecolor=tuple(col),
                 markeredgecolor='k', markersize=5)
    plt.title('Proper Motion')
    plt.xlabel('pmra')
    plt.ylabel('pmdec')
    plt.axis('square')
    plt.show(2)
    '''
    
    
    
    fig5 = plt.figure(5)
    plt.clf()
    for k, col in zip(unique_labels, colors):
        if k == -1:
            continue
       # if k == 0:
       #     continue
        
        class_member_mask = (labels == k)
        
        xy = Data[class_member_mask & core_samples_mask]
        plt.plot(xy.BP_RP, xy.Gmag, 'o', markerfacecolor=tuple(col),
                     markeredgecolor='k', markersize=9)
        #print(xy)
        xy = Data[class_member_mask & ~core_samples_mask]
        plt.plot(xy.BP_RP, xy.Gmag, 'o', markerfacecolor=tuple(col),
                 markeredgecolor='k', markersize=5)
    
    plt.title('Color-mag')
    plt.xlabel('bp-rp')
    plt.ylabel('Gmag')
    #plt.hlines(19, 1.3, 3.4, color = 'r')
    #plt.xlim([1.2,3.5])
    y1,y2=plt.gca().get_ylim()
    x1,x2=plt.gca().get_xlim()
    plt.gca().invert_yaxis()
    plt.show(5)
    
    
    
    
    '''
    fig3 = plt.figure(3)
    ax = fig3.add_subplot(111, projection='3d')
    col_list = list(mcolors.CSS4_COLORS.keys())
    for k, col in zip(unique_labels, colors):
        if k == -1:
            continue
        else:
            dot_color = random.choice(col_list)
            class_member_mask = (labels == k)
        
            xy = main_data[class_member_mask & core_samples_mask]
            L = xy.l.to_numpy()/(180/math.pi)
            B = xy.b.to_numpy()/(180/math.pi)
            R = xy.par.to_numpy()
            X = R*np.cos(L)*np.cos(B)
            Y = R*np.sin(L)*np.cos(B)
            Z = R*np.sin(B)
            ax.scatter(X, Y, Z, s=11, c=dot_color, marker='o')

            xy = main_data[class_member_mask & ~core_samples_mask]
            L = xy.l.to_numpy()/(180/math.pi)
            B = xy.b.to_numpy()/(180/math.pi)
            R = xy.par.to_numpy()
            X = R*np.cos(L)*np.cos(B)
            Y = R*np.sin(L)*np.cos(B)
            Z = R*np.sin(B)
            ax.scatter(X, Y, Z, s=6, c=dot_color, marker='o')

    ax.scatter([0], [0], [0], s=20, c='y', marker='*')
    plt.show(3)
    
    fig4 = plt.figure(4)
    col_list = list(mcolors.CSS4_COLORS.keys())
    for k, col in zip(unique_labels, colors):
        if k == -1:
            continue
        else:
            dot_color = random.choice(col_list)
            class_member_mask = (labels == k)
        
            xy = main_data[class_member_mask & core_samples_mask]
            L = xy.l.to_numpy()/(180/math.pi)
            B = xy.b.to_numpy()/(180/math.pi)
            R = xy.par.to_numpy()
            X = R*np.cos(L)*np.cos(B)
            Y = R*np.sin(L)*np.cos(B)
            plt.plot(Y, -X, 'o', markerfacecolor=dot_color,
                     markeredgecolor='k', markersize=9)

            xy = main_data[class_member_mask & ~core_samples_mask]
            L = xy.l.to_numpy()/(180/math.pi)
            B = xy.b.to_numpy()/(180/math.pi)
            R = xy.par.to_numpy()
            X = R*np.cos(L)*np.cos(B)
            Y = R*np.sin(L)*np.cos(B)
            plt.plot(Y, -X, 'o', markerfacecolor=dot_color,
                     markeredgecolor='k', markersize=5)

    plt.plot([0],[0], '*y', markersize=15)
    plt.title('Galactic Plane. GC is at the bottom')
    plt.axis('square')
    plt.show(4)

    fig5 = plt.figure(5)
    col_list = list(mcolors.CSS4_COLORS.keys())
    for k, col in zip(unique_labels, colors):
        if k == -1:
            continue
        else:
            dot_color = random.choice(col_list)

            class_member_mask = (labels == k)
        
            xy = main_data[class_member_mask & core_samples_mask]
            B = xy.b.to_numpy()/(180/math.pi)
            R = xy.par.to_numpy()
            X = R
            Y = R*np.sin(B)
            plt.plot(X, Y, 'o', markerfacecolor=dot_color,
                     markeredgecolor='k', markersize=9)

            xy = main_data[class_member_mask & ~core_samples_mask]
            B = xy.b.to_numpy()/(180/math.pi)
            R = xy.par.to_numpy()
            X = R
            Y = R*np.sin(B)
            plt.plot(X, Y, 'o', markerfacecolor=dot_color,
                     markeredgecolor='k', markersize=5)

    plt.plot([0],[0], '*y', markersize=15)
    plt.title('R-Z')
    plt.xlabel('R')
    plt.ylabel('Z')
    plt.show(5)
    '''
    

#a=(max(xy.RA_ICRS)-min(xy.RA_ICRS))/2
#b=(max(xy.DE_ICRS)-min(xy.DE_ICRS))/2
#print('%.2f' % a,'%.2f' % b, '%.2f' % math.sqrt(a*a+b*b))
#print('Mean values: pmRA:','%.2f' %  np.mean(xy.pmRA),'pmDE:','%.2f' % np.mean(xy.pmDE), 'parallax:','%.3f' % np.mean(xy.Plx), 'RA_ICRS:','%.2f' % np.mean(xy.RA_ICRS), 'DE_ICRS:','%.2f' % np.mean(xy.DE_ICRS))
#print('\n','%.2f' %  np.mean(xy.RA_ICRS),'%.2f' % np.mean(xy.DE_ICRS),'\n')
#print('\n','%.2f' %  np.mean(xy.pmRA),'%.2f' % np.mean(xy.pmDE), '%.3f' % np.mean(xy.Plx),'%.2f' % np.mean(xy.RA_ICRS),'%.2f' % np.mean(xy.DE_ICRS),'\n')
#ans ='\t\t'+str(int(args.N_DBSCAN))+' & '+str('%.2f' %  np.mean(xy.RA_ICRS))+'('+str('%.2f' % a)+')'+' & '+str('%.2f' % np.mean(xy.DE_ICRS))+'('+str('%.2f' % b)+')'+' & '+str('%.2f' % math.sqrt(a*a+b*b))+' & '+str('%.2f' % np.mean(xy.DE_ICRS))
#print(ans)
#pyperclip.copy(ans)
#print(args.input_data, args.N_DBSCAN, args.Eps_DBSCAN)

#       81 &   $11.80(0.2)$ & $60.01(0.2)$ & $0.02$ & $0.04(0.01)$  & $-1.53(0.56)$ & $-0.07(0.71)$  \\
#		\midrule
#limit=10



