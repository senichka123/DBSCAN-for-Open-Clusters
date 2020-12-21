import doctest
import unittest
import pandas as pd
import tempfile

from ocscan.download import gaiadata

class NumberOfClustersTestCase(unittest.TestCase):
	def test_columnname(self):
		Data = gaiadata(124.90, -38.27, save_data = True)
		a = list(Data)
		actual = [a[0],a[1],a[4],a[6],a[8]]
		desired = ['RA_ICRS', 'DE_ICRS', 'Plx', 'pmRA', 'pmDE']
		assert actual == desired
if __name__ == '__main__':

    unittest.main()
