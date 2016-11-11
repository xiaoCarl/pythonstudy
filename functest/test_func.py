

import unittest
from  demofunc import testdemo

class DemofuncTestCase(unittest.TestCase):
    
	"""Tests for `demofunc.py' """
	def test_is_demo(self):

		"""Show arg """
                testdemo(1,2,x=3)
 
		self.assertTrue( True )


	def test_is_demo2(self):
                 
                testdemo(2,3,y=['a'])
  
		self.assertTrue( True )



if __name__ == '__main__':

    unittest.main()
