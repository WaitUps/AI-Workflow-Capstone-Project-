
import unittest
import sys, os, getopt


try:
    optlist, args = getopt.getopt(sys.argv[1:],'v')
except getopt.GetoptError:
    print(getopt.GetoptError)
    print(sys.argv[0] + "-v")
    print("... the verbose flag (-v) may be used")
    sys.exit()

VERBOSE = False
RUNALL = False

sys.path.append(os.path.realpath(os.path.dirname(__file__)))

for o, a in optlist:
    if o == '-v':
        VERBOSE = True


from model_test import *

# model tests
ModelTestSuite = unittest.TestLoader().loadTestsFromTestCase(ModelTest)
MainSuite = unittest.TestSuite([ModelTestSuite])
