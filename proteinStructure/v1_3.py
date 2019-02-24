import numpy as np
import os,glob
import vpython

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


#print(x)
print("Alpha Carbons")
for element in x:
    for point in element:
        print(point)

''''                
                 for counter_2 in range(1,len(x[j])):

                     if (x[j][counter_2].__contains__(word)):
                      #print(x[j][counter_2])
                      counter_3 =  True
                      break
                 if(counter_3):
                     break
'''

angles = []
vectors = []
#angles_2 = []
i=-1
for element in x:
    i+=1
    angles.append([element[0]])
    for point in range(0,len(element)):

        if point == len(element)-3:
            break

        a = np.array([float(element[point+1][3]), float(element[point+1][4]), float(element[point+1][5])])
        b = np.array([float(element[point+2][3]), float(element[point+2][4]), float(element[point+2][5])])
        c = np.array([float(element[point+3][3]), float(element[point+3][4]), float(element[point+3][5])])


        ba = a - b
        bc = c - b

        cosine_angle = np.dot(ba, bc) / (np.linalg.norm(ba) * np.linalg.norm(bc))
        #print(cosine_angle)
        angle = np.arccos(cosine_angle)

        #ann = vpython.vector(-2.05 , -1.247 , 2.976).diff_angle(vpython.vector(-0.191 , 3.68 ,  1.014))
        #print(ba)
        #print(bc)
        #angles_2.append(vpython.degrees(ann))


        #print(np.degrees(angle))
        angles[i].append(np.degrees(angle))

i=-1
for element in x:
    i += 1
    vectors.append([element[0]])
    for point in range(0,len(element)):
        
        if point == len(element)-2:
            break

        a = np.array([float(element[point + 1][3]), float(element[point + 1][4]), float(element[point + 1][5])])
        b = np.array([float(element[point + 2][3]), float(element[point + 2][4]), float(element[point + 2][5])])

        a_2 = vpython.vector(b[0]-a[0], b[1]-a[1], b[2]-a[2])

        vectors[i].append(a_2)
       
print("Angles")
for element in angles:
    for point in element:
        print(point)

#print(angles_2)
#print(len(x[0])+len(x[1])+len(x[2]))
#print(len(vectors))
#v1 = vpython.vector( 3.042 , 0.594, -2.146)
#gg = vpython.rotate(v1,angle=vpython.radians(angles[0]),axis=vpython.vector(1,1,1))
#print(v1)
#print(gg)
#print(vectors)

print("Vectors")
for element in vectors:
    for point in element:
        print(point)

vectors_mag = []


i=-1
for element in vectors:
    i += 1
    vectors_mag.append([element[0]])
    for point in range(0, len(element)):

        if point == len(element)-1:
            break

        vectors_mag[i].append(vpython.mag(element[point + 1]))


print("Vector Magnitudes")
for element in vectors_mag:
    for point in element:
        print(point)


i=-1
trans_vectors = []

for element in x:
    i += 1
    trans_vectors.append([element[0]])
    for point in range(0, len(element)):


        if point == len(element)-1:
            break

        a = np.array([float(element[point+1][3]), float(element[point+1][4]), float(element[point+1][5])])
        b = np.array([float(element[1][3]), float(element[1][4]), float(element[1][5])])



        trans_vectors[i].append(a - b)

print("Transformed Points")
for element in trans_vectors:
    for point in element:
        print(point)


