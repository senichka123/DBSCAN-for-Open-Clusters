import doctest
import unittest
import pandas as pd
import sys

from ocscan.dbscan import dbscan
from ocscan.download import gaiadata
from ocscan.show import NumberOfClusters

class NumberOfClustersTestCase(unittest.TestCase):
	def test_result(self):
		data = gaiadata(124.90, -38.27)
		mytuple = dbscan(data, 22, 0.3)
		actual = NumberOfClusters(mytuple[1])
		desired = 1
		assert actual == desired, f'Estimated number of clusters: {actual} != {desired}'

if __name__ == '__main__':

    unittest.main()
