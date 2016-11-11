#!/usr/bin/env python

def testdemo( arg1,arg2,*nkw,**kw):
	print 'arg1 is:',arg1
	print 'arg2 is:',arg2
        for eachNKW in nkw:
		print 'additional non-keyword arg:', eachNKW
	for eachKW in kw.keys():
		print "addition keyword arg '%s': %s" %(eachKW,kw[eachKW])
        return True
  

if __name__ =='__main__':

	print "testdemo(1,2,['a','b'])"
	testdemo(1,2,['a','b'])

	print "testdemo(1,2,x=3)"
	testdemo(1,2,x=3)

	print "testdemo(1,2,x=['a>1.0'],y=True)"
	testdemo(1,2,x=['a>1.0'],y=True)

	print "testdemo(1,2,**{'a':10,'b':19})"
	testdemo(1,2,**{'a':10,'b':19})

	print "testdemo(1,2,*('a','b'))"
	testdemo(1,2,*('a','b'))
