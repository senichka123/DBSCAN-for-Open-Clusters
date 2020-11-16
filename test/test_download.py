import doctest
import unittest
import pandas as pd

from bin.download import gaiadata

class NumberOfClustersTestCase(unittest.TestCase):
	def test_datasize(self):
		actual= gaiadata(124.90, -38.27)
		desired = pd.read_csv('data.csv')
		assert actual.size == desired.size

	def test_columnname(self):
		Data = gaiadata(124.90, -38.27)
		a = list(Data)
		actual = b = [a[0],a[1],a[4],a[6],a[8]]
		desired = ['RA_ICRS', 'DE_ICRS', 'Plx', 'pmRA', 'pmDE']
		assert actual == desired
if __name__ == '__main__':

    unittest.main()