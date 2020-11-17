import doctest
import unittest
import pandas as pd
import sys

from ocscan.dbscan import dbscan
from ocscan.show import NumberOfClusters

class NumberOfClustersTestCase(unittest.TestCase):
	def test_result(self):
		labels = dbscan(22, 0.3, 124.90, -38.27, plot=False, save=False)
		actual = NumberOfClusters(labels)
		desired = 1
		assert actual == desired, f'Estimated number of clusters: {actual} != {desired}'

if __name__ == '__main__':

    unittest.main()