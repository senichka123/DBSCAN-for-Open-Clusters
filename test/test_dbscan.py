import doctest
import unittest
import pandas as pd
import sys

from bin.dbscan import dbscan
from bin.dbscan import _parse_args

class NumberOfClustersTestCase(unittest.TestCase):
	def test_result(self):
		actual = dbscan(22, 0.3, 124.90, -38.27)
		desired = 1
		assert actual == desired, f'Estimated number of clusters: {actual} != {desired}'

if __name__ == '__main__':

    unittest.main()