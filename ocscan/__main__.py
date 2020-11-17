import argparse as ap
# general packages

import ocscan.show
import ocscan.dbscan
# my modules



def _parse_args(args=None):
	"""Parse command line arguments"""

	parser=ap.ArgumentParser(description = 'Searching for clusters in data on the basis of DBSCAN algorithm and Principal Component Analysis in 4-dimensional space')
	parser.add_argument('-N', default = 22, help='number of neighbours', type = int)
	parser.add_argument('-e', '--eps', default = 0.3, help='radius of hyper-sphere in 4D space', type = float)
	parser.add_argument('-r', '--ra', default = 124.90, help='right accession', type = float)
	parser.add_argument('-d', '--de', default = -38.27, help='declination', type = float)
	parser.add_argument('-p', '--plot', action='store_true', help='plot graphs')
	parser.add_argument('-s', '--saveresults', action='store_true', help='saving results into .csv files')
	namespace = parser.parse_args()
	return namespace

def main():
	p = _parse_args()
	labels = ocscan.dbscan(p.N, p.eps, p.ra, p.de, p.plot, p.saveresults)
	ocscan.show.NumberOfClusters(labels)

if __name__ == '__main__':	
	main()
	