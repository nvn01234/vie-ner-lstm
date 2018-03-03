from __future__ import print_function
import sys

py3 = sys.version_info > (3, 0)
py2 = not py3
if py3:
    import pickle
else:
    import cPickle as pickle


def iteritems(a):
    return a.iters() if py3 else a.iteritems()
