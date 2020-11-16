import doctest
import unittest
import pandas as pd

from bin.download import gaiadata

class NumberOfClustersTestCase(unittest.TestCase):
	def test_datasize(self):
		actual, b = gaiadata(124.90, -38.27)
		desired = pd.read_csv('data.csv')
		assert actual.size == desired.size

	def test_columnname(self):
		a, actual = gaiadata(124.90, -38.27)
		desired = ['RA_ICRS', 'DE_ICRS', 'Plx', 'pmRA', 'pmDE']
		assert actual == desired
if __name__ == '__main__':

    unittest.main()