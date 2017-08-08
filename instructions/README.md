# Tutorial to get API Credentials

Go to https://console.cloud.google.com/ and follow the next instructions:
 * Create a project and name it.
 * Select that project from the pop-up menu `Select a project`.
 * On the Main Menu (top left 3 vertical lines) click on `APIs and Services` and then `Library`.

![alt text][s1]

* Under `Google Cloud Machine Learning` click on `Vision API`.


![alt text][s2]


* Click on button `ENABLE` (if you have not created the billing account yet it will ask you to create one).


![alt text][s3]

* On the left Menu click `Credentials`.

![alt text][s4]

* The `Create Credentials` button will pop up a list of different types of Credentials: select `Service account  key.`


![alt text][s5]

* Create a `New service account` and fill the `Service account name` field and the `Role` field (that can be Project->Owner). Select as `Key type` JSON and finish with the button `Create`. A .json file will be instantly downloaded and saved locally. ***Put that file in the repository folder***

![alt text][s6]









[s1]: https://raw.githubusercontent.com/charlielito/vision-sentiment-analysis-googleapi/master/output/output_Happy.jpg "S"
[s2]: https://raw.githubusercontent.com/charlielito/vision-sentiment-analysis-googleapi/master/output/output_Surprised.jpg "S"
[s3]: https://raw.githubusercontent.com/charlielito/vision-sentiment-analysis-googleapi/master/output/output_Sad.jpg "S"
[s4]: https://raw.githubusercontent.com/charlielito/vision-sentiment-analysis-googleapi/master/output/output_Angry.jpg "S"
[s5]: https://raw.githubusercontent.com/charlielito/vision-sentiment-analysis-googleapi/master/output/output_Happy.jpg "S"
[s6]: https://raw.githubusercontent.com/charlielito/vision-sentiment-analysis-googleapi/master/output/output_Surprised.jpg "S"
