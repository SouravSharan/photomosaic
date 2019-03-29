import argparse
import cv2
import os, sys
import numpy as np
import imutils
from imutils.paths import list_images
import pickle
import rgbhist
import searchIndex as si

ap = argparse.ArgumentParser()
ap.add_argument("-v", "--videoPath", required = True, help = "Path to the input video")
ap.add_argument("-p", "--posterPath", required = True, help = "Path to the input poster")
args = vars(ap.parse_args())

cap =cv2.VideoCapture(args["videoPath"])
length = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
fps = int(cap.get(cv2.CAP_PROP_FPS))
print( length )
print( fps )

skip  = 0
x=0
ix = 3000
iy = 3000
tx = 25
ty = 25

dataPath = ""

dataPath = os.path.splitext(os.path.basename(args["videoPath"]))[0] + "/"
try:
    os.mkdir(dataPath)
except:
    dataPath = os.path.splitext(os.path.basename(args["videoPath"]))[0] + "/"
    
while True:
    cap.set(0,84000+skip)
    skip+=5500
    print(skip)
    ret, img = cap.read()
    if ret != True:
        break
    img = cv2.resize(img, (tx, ty)) 
    cv2.imwrite(dataPath + str(x)+ ".png", img)
    x+=1

index = {}
desc = rgbhist.RGBHistogram([8, 8, 8])
for imagePath in list_images(dataPath):
	k = imagePath[imagePath.rfind("/") + 1:]
	image = cv2.imread(imagePath)
	features = desc.describe(image)
	index[k] = features
	
f = open("index" + os.path.splitext(os.path.basename(args["videoPath"]))[0] + ".cpickle", "wb")
f.write(pickle.dumps(index))
f.close()
 
print("[INFO] done...indexed {} images".format(len(index)))

img = cv2.imread(args["posterPath"])
print(img.shape)
img = cv2.resize(img, (iy, ix)) 
print(img.shape)
fin = np.zeros((ix,iy,3))
print(fin.shape)

index = pickle.loads(open("index.cpickle", "rb").read())
searcher = si.Searcher(index)

for i in range(0,ix,tx):
    for j in range(0,iy,ty):
        target = img[i:i+tx, j:j+ty, 0:3]        
        targetFeatures = desc.describe(target)
        (imageName, score) = searcher.search(targetFeatures)
        path = os.path.join(dataPath, imageName)
        result = cv2.imread(path)
        print(path + " " + str(score))
        fin[i:i+tx, j:j+ty, 0:3] = result
        cv2.imwrite("save.png", fin)
cv2.imwrite("save.png", fin)

