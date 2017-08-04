import cv2
import numpy as np
import argparse
# Imports the Google Cloud client library
from google.cloud import vision

#Emotions
emo = ['Angry', 'Surprised','Sad', 'Happy']
string = 'No sentiment'
############## Spanish version #################
#emo = ['Bravo', 'Sorprendido','Triste', 'Feliz']
#string = 'Sin emocion'

# construct the argument parse and parse the arguments
ap = argparse.ArgumentParser(description='Process some image to find sentiment in faces (if any)')
ap.add_argument("-f", "--file_name", required=False, default="imgs/angry.jpg", help="path to image")
args = vars(ap.parse_args())

file_name = args["file_name"]

# Instantiates a client
vision_client = vision.Client()

image = vision_client.image(filename=file_name)

faces = image.detect_faces(limit=20)
print 'Number of faces: ', len(faces)

img = cv2.imread(file_name)

for face1 in faces:

    x = face1.fd_bounds.vertices[0].x_coordinate
    y = face1.fd_bounds.vertices[0].y_coordinate
    x2 = face1.fd_bounds.vertices[2].x_coordinate
    y2 = face1.fd_bounds.vertices[2].y_coordinate

    cv2.rectangle(img, (x, y), (x2, y2), (0, 255, 0), 2)

    sentiment = [face1.anger.value,face1.surprise.value,face1.sorrow.value,face1.joy.value]
    for item, item2 in zip(emo, sentiment):
        print item, ": ", item2

    if not (all( item == 'VERY_UNLIKELY' for item in sentiment) ):

        if any( item == 'VERY_LIKELY' for item in sentiment):
            state = sentiment.index('VERY_LIKELY')
            # the order of enum type Likelihood is:
            #'LIKELY', 'POSSIBLE', 'UNKNOWN', 'UNLIKELY', 'VERY_LIKELY', 'VERY_UNLIKELY'
            # it makes sense to do argmin if VERY_LIKELY is not present, one would espect that VERY_LIKELY
            # would be the first in the order, but that's not the case, so this special case must be added
        else:
            state = np.argmin(sentiment)

        string = emo[state]

    cv2.putText(img,string, (x,y-5), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0,0,255), 2)

cv2.imshow("Video", img)
cv2.waitKey(0)
cv2.imwrite('output/output_'+string+'.jpg',img)
