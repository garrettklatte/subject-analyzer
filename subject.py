#! /usr/bin/python

import sys
import numpy
from os import listdir
from os import path
from collections import defaultdict

if len(sys.argv) != 2:
    print "ERROR: subject.py <directory>"
    sys.exit()

directory = sys.argv[1]
cutoffdate = "2017-09-24"
dic = defaultdict(list)
delimiter = "_"

for subject in listdir(directory):
    tokens = subject.split(delimiter)
    dic[tokens[0]].append(subject)

print "USERID    PRE   POST"
for userid, filelist in dic.iteritems():
    presizelist = list()
    postsizelist = list()
    for filename in filelist:
        tokens = filename.split(delimiter)
        filename = path.join(directory, filename)

        if tokens[1] < cutoffdate:
            presizelist.append(path.getsize(filename))
        else:
            postsizelist.append(path.getsize(filename))
            
    print str(userid).ljust(9), str(numpy.mean(presizelist)).ljust(5), numpy.mean(postsizelist)
