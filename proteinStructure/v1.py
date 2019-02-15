import numpy as np
import matplotlib.pyplot as plt
import csv
from mpl_toolkits import mplot3d
from mpl_toolkits.mplot3d import Axes3D
from mpl_toolkits.mplot3d import axes3d
from matplotlib.colors import LightSource
from matplotlib import cm
import os,glob

#x = list()
#y = list()
#z = list()

x = []
i=0
counter = 0
j=-1
for filename in glob.glob(os.path.join('*.pdb')):
    j = j + 1
    x.append([filename])
    i = 0
    counter = 0
    with open(filename,'r') as f:
        for line in f:
            #print(line)
            a = i
            counter = 0
            if(line.__contains__("ATOM") and line.__contains__("CA")):
               x[j].append(["CA"])
               #print(x)
               i = i + 1
               #print(x[a][1])
            #x.append(i)
            #i = i + 1

            for word in line.split():
               if line.__contains__("ATOM") and line.__contains__("CA"):

                #print(x[0][0])
                counter = counter + 1
                if (counter == 2):
                 if (x.__contains__(word)):
                     break
                 x[j][a+1].append(word)
                elif(counter == 4):
                 x[j][a+1].append(word)
                elif (counter == 7):
                 x[j][a+1].append(word)
                elif (counter == 8):
                 x[j][a+1].append(word)
                elif (counter == 9):
                 x[j][a+1].append(word)


               #x[i].append(word)
               #print(word)


print(x)
