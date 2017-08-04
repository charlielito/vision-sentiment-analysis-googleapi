import cv2
import numpy as np
# Imports the Google Cloud client library
from google.cloud import vision


#Emotions
emo = ['Angry', 'Surprised','Sad', 'Happy']
string = 'No sentiment'
############## Spanish version #################
#emo = ['Bravo', 'Sorprendido','Triste', 'Feliz']
#string = 'Sin emocion'

# Instantiates a client
vision_client = vision.Client()

# The name of the image file to annotate

cv2.imshow('Video', np.empty((5,5),dtype=float))
compressRate = 1
while cv2.getWindowProperty('Video', 0) >= 0:
    video_capture = cv2.VideoCapture(0)
    ret, img = video_capture.read()
    img = cv2.resize(img, (0,0), fx=compressRate , fy=compressRate )

    ok, buf = cv2.imencode(".jpeg",img)
    image = vision_client.image(content=buf.tostring())

    faces = image.detect_faces(limit=20)
    print 'Number of faces: ', len(faces)
    for i in range(0,len(faces)):
        face1 = faces[i]
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
    cv2.waitKey(1)
    video_capture.release()

# When everything is done, release the capture
cv2.destroyAllWindows()
