import numpy as np
import os,glob


x = []
i=0
counter = 0
j=-1
#counter_3 = False

for filename in glob.glob(os.path.join('*.pdb')):
    j = j + 1
    x.append([filename])
    i = 0
    counter = 0
    #counter_3 = False
    with open(filename,'r') as f:
        for line in f:
            #if (counter_3):
                #print("first")
                #print(counter_3)
                #break

            #print(line)
            a = i
            counter = 0

            if line.__contains__("ENDMDL"):
                break

            if(line.__contains__("ATOM") and line.__contains__("CA")):
               x[j].append(["CA"])
               i = i + 1

            for word in line.split():
               if line.__contains__("ATOM") and line.__contains__("CA"):

                #print(x[0][0])
                counter = counter + 1
                if (counter == 2):
                 x[j][a + 1].append(word)
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

''''                
                 for counter_2 in range(1,len(x[j])):

                     if (x[j][counter_2].__contains__(word)):
                      #print(x[j][counter_2])
                      counter_3 =  True
                      break
                 if(counter_3):
                     break
'''
#result = atan2(P3.y - P1.y, P3.x - P1.x) -
#                atan2(P2.y - P1.y, P2.x - P1.x);
''''
a = np.array([ 5.166, -0.026, -4.647])
b = np.array([ 5.968, -0.352, -0.96 ])
c = np.array([ 3.603, -0.011,  1.971])
print(a)
print(b)
print(c)
ba = a - b
bc = c - b
print(ba)
print(bc)
cosine_angle = np.dot(ba, bc) / (np.linalg.norm(ba) * np.linalg.norm(bc))
print(cosine_angle)
angle = np.arccos(cosine_angle)

print(np.degrees(angle))
'''
angles = []

for element in x:
    for point in range(0,len(element)):

        if point == len(element)-3:
            break

        a = np.array([float(element[point+1][3]), float(element[point+1][4]), float(element[point+1][5])])
        b = np.array([float(element[point+2][3]), float(element[point+2][4]), float(element[point+2][5])])
        c = np.array([float(element[point+3][3]), float(element[point+3][4]), float(element[point+3][5])])
        #print("numbers")
        #print(a)
        #print(b)
        #print(c)
        ba = a - b
        bc = c - b
        #print(ba)
        #print(bc)
        cosine_angle = np.dot(ba, bc) / (np.linalg.norm(ba) * np.linalg.norm(bc))
        #print(cosine_angle)
        angle = np.arccos(cosine_angle)

        #print(np.degrees(angle))
        angles.append(np.degrees(angle))


print(angles)
#print(len(x[0])+len(x[1])+len(x[2]))
#print(len(angles))