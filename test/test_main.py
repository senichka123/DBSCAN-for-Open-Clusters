import doctest
import unittest
import pandas as pd
import sys

from bin.__main__ import main

class NumberOfClustersTestCase(unittest.TestCase):
	def test_result(self):
		#sys.argv[0]
		actual = main()
		desired = 1
		assert actual == desired, f'Estimated number of clusters: {actual} != {desired}'

if __name__ == '__main__':

    unittest.main()