# Sentiment Analysis with images using Google Vision Api



![alt text][s1] ![alt text][s2] ![alt text][s3] ![alt text][s4]



## Requirements
* Python 2.7
* OpenCV 3.0+ with python bindings (needed to visualize the images/video)
* Numpy
* Google Cloud client python library
* ***Google Vision Api Credentials***

To install the python dependences just execute:

```
pip install -R requirements.txt
```

You need the ***Google Vision Api Credentials***, therefore an account and a project must be created in google cloud portal and the vision service need to be added to that project. At the end you will get a `credentials.json` file with the whole information. For more info about this step go to [Authenticating to the Cloud Vision API](https://cloud.google.com/vision/docs/auth).



## Usage

Before you can call the api for visual recognition, the path to the credentials json file must be specified in the enviromental variable `GOOGLE_APPLICATION_CREDENTIALS`. Just execute for example:
```
export GOOGLE_APPLICATION_CREDENTIALS=credentials.json
```


### Feed from Webcam

This script gets feed from the first Webcam that identifies and analyses it, if faces are found it displays where the faces are and their corresponding emotion (if any). Just execute

```
python main.py
```

### Specific image

The same can be done to a specific image given a path. It would show the result and after the window is closed, in the `output` folder would be saved the annotated image with the detected faces and their emotions. Type:

```
python main_image.py -f imgs/people.jpg
```


[s1]: https://raw.githubusercontent.com/charlielito/vision-sentiment-analysis-googleapi/master/output/output_Happy.jpg "S"
[s2]: https://raw.githubusercontent.com/charlielito/vision-sentiment-analysis-googleapi/master/output/output_Surprised.jpg "S"
[s3]: https://raw.githubusercontent.com/charlielito/vision-sentiment-analysis-googleapi/master/output/output_Sad.jpg "S"
[s4]: https://raw.githubusercontent.com/charlielito/vision-sentiment-analysis-googleapi/master/output/output_Angry.jpg "S"
