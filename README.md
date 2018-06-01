# Sentiment Analysis with images using Google Vision Api

Application of image recognition to find people in images and analyze their sentiments or emotions. This repo uses the Vision services of Google platform to perform that task. Given an image, it would search for faces, identify them, put a rectangle in their positions and described the emotion found. Some examples are shown below.

##### From Webcam Feed
![alt text][s6]


##### From specific images
![alt text][s5] ![alt text][s1] ![alt text][s2] ![alt text][s4] ![alt text][s3]


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

You need the ***Google Vision Api Credentials***, therefore an account and a project must be created in google cloud portal and the vision service need to be added to that project. At the end you will get a `credentials.json` file with the whole information. For more info about this step go to [Authenticating to the Cloud Vision API](https://cloud.google.com/vision/docs/auth) and [Google Application Default Credentials](https://developers.google.com/identity/protocols/application-default-credentials) or follow the next instructions.


### Easy tutorial to get API Credentialss

***Important: You need an account in Google Cloud Platform (an email works) and a billing account registered to it (credit card). They wont charge anything unless your free trial expires and you have one year free and also 300 USD to use it for free in the platform.***

Go to https://console.cloud.google.com/ and follow the next instructions:
 * Create a project and name it.
 * Select that project from the pop-up menu `Select a project`.
 * On the Main Menu (top left 3 vertical lines) click on `APIs and Services` and then `Library`.
 * Under `Google Cloud Machine Learning` click on `Vision API`.
 * Click on button `ENABLE` (if you have not created the billing account yet it will ask you to create one).
 * On the left Menu click `Credentials`.
 * The `Create Credentials` button will pop up a list of different types of Credentials: select `Service account  key.`
 * Create a `New service account` and fill the `Service account name` field and the `Role` field (that can be Project->Owner). Select as `Key type` JSON and finish with the button `Create`. A .json file will be instantly downloaded and saved locally. ***Put that file in the repository folder***

For a visual tutorial go to the [Instructions](https://github.com/charlielito/vision-sentiment-analysis-googleapi/tree/master/instructions) folder from this repository.

## Usage

Before you can call the api for visual recognition, the path to the credentials json file must be specified in the environment variable `GOOGLE_APPLICATION_CREDENTIALS`. Just execute for example:
```
export GOOGLE_APPLICATION_CREDENTIALS="/path/to/keyfile.json"
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


 ***Note:*** You have 1000 image analyses free per month plus your 300 USD from the free trial.


### Troubleshooting

If you had some problems running it with some auth library, try the following.

```
pip install --upgrade google-auth-oauthlib
```

If you had troubles installing the google cloud client with pip v10, try it with v9.

[s1]: https://raw.githubusercontent.com/charlielito/vision-sentiment-analysis-googleapi/master/output/output_Happy.jpg "S"
[s2]: https://raw.githubusercontent.com/charlielito/vision-sentiment-analysis-googleapi/master/output/output_Surprised.jpg "S"
[s3]: https://raw.githubusercontent.com/charlielito/vision-sentiment-analysis-googleapi/master/output/output_Sad.jpg "S"
[s4]: https://raw.githubusercontent.com/charlielito/vision-sentiment-analysis-googleapi/master/output/output_Angry.jpg "S"
[s5]: https://raw.githubusercontent.com/charlielito/vision-sentiment-analysis-googleapi/master/output/output_No%20sentiment.jpg "S"

[s6]: https://raw.githubusercontent.com/charlielito/vision-sentiment-analysis-googleapi/master/imgs/Emotions.gif "gifsito"


