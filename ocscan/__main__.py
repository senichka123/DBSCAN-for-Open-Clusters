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
	parser.add_argument('-i', '--saveinput', action='store_true', help='saving input file into .csv')
	parser.add_argument('-s', '--saveresults', action='store_true', help='saving results into .csv files')
	namespace = parser.parse_args()
	return namespace

def main():
	p = _parse_args()
	data = ocscan.download.gaiadata(p.ra, p.de, save_data=input)
	mytuple = ocscan.dbscan(data, p.N, p.eps, p.saveinput)
	ocscan.show.NumberOfClusters(mytuple[1])
	if p.plot:
		ocscan.plot.graphs(mytuple[0], mytuple[1], mytuple[2])
	if p.saveresults:
		ocscan.save.results(mytuple[0], mytuple[1], mytuple[2])

if __name__ == '__main__':	
	main()
	
