import cv2
import numpy as np
# Imports the Google Cloud client library
from google.cloud import vision

#Emotions
emo = ['Angry', 'Surprised','Sad', 'Happy', "Under Exposed", "Blurred", "Headwear"]
likelihood_name = ('UNKNOWN', 'VERY_UNLIKELY', 'UNLIKELY', 'POSSIBLE',
                    'LIKELY', 'VERY_LIKELY')

############## Spanish version #################
#emo = ['Bravo', 'Sorprendido','Triste', 'Feliz']
#string = 'Sin emocion'

#from google.oauth2 import service_account
#credentials = service_account.Credentials.from_service_account_file('VisionApp-9cb3e521631b.json')

# Instantiates a client
vision_client = vision.ImageAnnotatorClient()

cv2.imshow('Video', np.empty((5,5),dtype=float))
compressRate = 1
while cv2.getWindowProperty('Video', 0) >= 0:
    video_capture = cv2.VideoCapture(0)
    ret, img = video_capture.read()
    img = cv2.resize(img, (0,0), fx=compressRate , fy=compressRate )

    ok, buf = cv2.imencode(".jpeg",img)
    image = vision.types.Image(content=buf.tostring())

    response = vision_client.face_detection(image=image)
    faces = response.face_annotations
    print 'Number of faces: ', len(faces)
    for face in faces:
        x = face.bounding_poly.vertices[0].x
        y = face.bounding_poly.vertices[0].y
        x2 = face.bounding_poly.vertices[2].x
        y2 = face.bounding_poly.vertices[2].y
        cv2.rectangle(img, (x, y), (x2, y2), (0, 255, 0), 2)

        sentiment = [likelihood_name[face.anger_likelihood],
                    likelihood_name[face.surprise_likelihood],
                    likelihood_name[face.sorrow_likelihood],
                    likelihood_name[face.joy_likelihood],
                    likelihood_name[face.under_exposed_likelihood],
                    likelihood_name[face.blurred_likelihood],
                    likelihood_name[face.headwear_likelihood]]

        for item, item2 in zip(emo, sentiment):
            print item, ": ", item2

        string = 'No sentiment'

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
