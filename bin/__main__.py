import bin.download
import bin.plotgraphs
import bin.dbscan
# my modules

from sklearn.cluster import DBSCAN
from sklearn.decomposition import PCA
import pandas as pd
import numpy as np
import argparse as ap
# general packages


def _parse_args(args=None):
	"""Parse command line arguments"""
	parser=ap.ArgumentParser(description = 'Searching for clusters in data on the basis of DBSCAN algorithm and Principal Component Analysis in 4-dimensional space')
	parser.add_argument('-N', default = 22, help='number of neighbours')
	parser.add_argument('-eps', default = 0.3, help='radius of hyper-sphere in 4D space')
	parser.add_argument('-ra', default = 124.90, help='right accession')
	parser.add_argument('-de', default = -38.27, help='declination')
	namespace = parser.parse_args()
	return namespace

if __name__ == '__main__':	
	p = _parse_args()
	Eps_DBSCAN=float(p.eps)
	N_DBSCAN=float(p.N)
	ra_download=float(p.ra)
	de_download=float(p.de)
	bin.dbscan(N_DBSCAN, Eps_DBSCAN, ra_download, de_download)
	